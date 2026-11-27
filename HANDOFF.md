# 引継ぎ資料: 01video-elevetor / Drive 転送

## 目的
PC 上のエレベーター動画プロジェクトの素材を Google Drive に入れ、GitHub リポジトリで管理する。

### 転送したいファイル（PC: DESKTOP-3L5VO46）
元のパス（C:\AI GN\6.elevator\...）から、現在は次の場所に移動済み:
`C:\Users\admin\OneDrive\Documents\AI_GN\6.elevator\`（※ 6.elevator 配下の構成は未確認）

- 参照画像: `refs`（フォルダごと）
- Blender ファイル: `elevator_v1.blend`
- Blender のショット動画: `ref_shot2_cab_shaft.mp4`、`ref_shot1_lobby_static.mp4`
- 上記以外に必要なファイルがあれば、確認して判断してコピーする（依頼内容）。

## 完了したこと
| 項目 | 状態 |
|---|---|
| `RCLONE_CONFIG_GDRIVE_TOKEN` を JSON 1つに修正 | 完了 |
| `rclone lsd gdrive:` | 成功。`video` フォルダが2つ見える（作成日時が違う） |
| rclone のインストール | 手動で apt により v1.60.1 を導入（旧セッションのみ） |
| 環境 `agent` のセットアップスクリプト | 追加済み: `command -v rclone >/dev/null \|\| (apt-get update; apt-get install -y rclone)`。新しいコンテナで動くか未検証 |
| GitHub リポジトリ作成 | 完了: https://github.com/Karasawauni/01video-elevetor （非公開、README 付き、ユーザー了承済み） |

## 未完了（本題）
PC のファイルを Drive に入れる作業が未実施。

### 詰まっている点
クラウドセッションから PC のフォルダに接続できない。`list_computer_folders` の結果が次の状態で変わらない。
- `folders`: 空
- `cannot_be_used`: DESKTOP-3L5VO46 の `AI_GN`（reason: `not_available`、PC 側は理由を返さない）

### 試して効果がなかったこと
- 共有フォルダ名の空白を除く（`AI GN` → `AI_GN`）
- C 直下から `C:\Users\admin\OneDrive\Documents\AI_GN` への移動と、Remote Control への再登録
- Claude デスクトップアプリの入れ直し

原因は不明。残る推測は、PC 側アプリのバージョン、または OneDrive 配下であること。

### 次の候補
1. 新セッションで `list_computer_folders` を再確認する。出ていれば `request_computer_folder` で接続し、`rclone copy` で Drive へ転送する。
2. 出なければ、PC 側のローカル Claude Code（PowerShell で対象フォルダに `cd` して `claude`）で作業する。PC 側にも rclone と Drive 認証が必要。
3. 最終手段: ユーザーが Drive にブラウザから直接アップロードし、その後の確認・整理・GitHub 反映を Claude が行う。

## 補足・注意
- Drive の保存先が未決定。`video` フォルダが2つあるので、中身を `rclone lsf` で見て決める。または新規に `01video-elevetor` フォルダを作る。
- `.blend` と動画は容量が大きいので、GitHub には入れず Drive に置く方針（ユーザーに確認済みではない）。GitHub には README などの管理用ファイルのみ入れる想定。
- rclone の認証は環境変数のみ（設定ファイルなし）。使う名前: `RCLONE_CONFIG_GDRIVE_TYPE` / `_SCOPE` / `_ROOT_FOLDER_ID` / `_TOKEN`。値は書かないこと。
- ユーザーの期待: Claude が自動でコピーまで行うこと。手動作業の依頼が続くことへの不満が強い。可能な限り自動で進める。
- このセッションの GitHub 権限は `karasawauni/agent` のみ。`01video-elevetor` を使うには `add_repo` で追加する。
