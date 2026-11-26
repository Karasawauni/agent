"""Modal で「プロンプト + 参照画像」から画像を生成するスクリプト。

モデル: Qwen/Qwen-Image-Edit-2509 (複数参照画像に対応 / Apache-2.0)

使い方:
    pip install modal && modal setup      # 初回のみ
    modal run scripts/modal_generate.py \
        --prompt "画像1の人物を画像2のエレベーター内に立たせる" \
        --refs "refs/person.png,refs/elevator.png" \
        --out out.png

    参照画像なし (テキストのみ) も可:
    modal run scripts/modal_generate.py --prompt "..." --out out.png

オプション: --seed 42 --steps 40 --cfg 4.0 --negative "..."
初回はモデルのダウンロードで数分かかる (Volume にキャッシュされ、2回目以降は速い)。
"""

import io
from pathlib import Path

import modal

MODEL_ID = "Qwen/Qwen-Image-Edit-2509"
CACHE_DIR = "/cache"

app = modal.App("image-gen-with-refs")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git")
    .pip_install(
        "torch",
        "transformers",
        "accelerate",
        "safetensors",
        "sentencepiece",
        "pillow",
        "huggingface_hub[hf_transfer]",
        # QwenImageEditPlusPipeline は新しい diffusers が必要
        "git+https://github.com/huggingface/diffusers.git",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1", "HF_HOME": CACHE_DIR})
)

cache_vol = modal.Volume.from_name("hf-cache-image-gen", create_if_missing=True)


@app.cls(
    image=image,
    gpu="H100",
    volumes={CACHE_DIR: cache_vol},
    timeout=60 * 30,
    scaledown_window=60 * 5,
)
class Generator:
    @modal.enter()
    def load(self):
        import torch
        from diffusers import QwenImageEditPlusPipeline

        self.pipe = QwenImageEditPlusPipeline.from_pretrained(
            MODEL_ID, torch_dtype=torch.bfloat16
        ).to("cuda")
        self.pipe.set_progress_bar_config(disable=None)
        cache_vol.commit()

    @modal.method()
    def generate(
        self,
        prompt: str,
        ref_images: list[bytes],
        negative: str = " ",
        seed: int = 0,
        steps: int = 40,
        cfg: float = 4.0,
    ) -> bytes:
        import torch
        from PIL import Image

        refs = [Image.open(io.BytesIO(b)).convert("RGB") for b in ref_images]
        kwargs = dict(
            prompt=prompt,
            negative_prompt=negative,
            true_cfg_scale=cfg,
            num_inference_steps=steps,
            generator=torch.manual_seed(seed),
            num_images_per_prompt=1,
        )
        if refs:
            kwargs["image"] = refs

        with torch.inference_mode():
            result = self.pipe(**kwargs).images[0]

        buf = io.BytesIO()
        result.save(buf, format="PNG")
        return buf.getvalue()


@app.local_entrypoint()
def main(
    prompt: str,
    refs: str = "",
    out: str = "out.png",
    negative: str = " ",
    seed: int = 0,
    steps: int = 40,
    cfg: float = 4.0,
):
    """refs はカンマ区切りで画像パスを複数指定できる。"""
    ref_paths = [p.strip() for p in refs.split(",") if p.strip()]
    ref_bytes = []
    for p in ref_paths:
        path = Path(p)
        if not path.is_file():
            raise SystemExit(f"参照画像が見つかりません: {p}")
        ref_bytes.append(path.read_bytes())

    print(f"prompt: {prompt}")
    print(f"refs: {len(ref_bytes)} 枚 / seed={seed} steps={steps} cfg={cfg}")

    png = Generator().generate.remote(
        prompt, ref_bytes, negative=negative, seed=seed, steps=steps, cfg=cfg
    )

    out_path = Path(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(png)
    print(f"保存しました: {out_path}")
