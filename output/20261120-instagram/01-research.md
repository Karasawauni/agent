# 01-research: Instagram Reels向け AI生成縦動画の流行調査（探索モード）

調査日: 2026-11-20 / 対象: Instagram（主にReels） / 検索: 14回（WebSearch）

## 0. 調査の制約（先に読む）
- `help.instagram.com` と `techcrunch.com` は WebFetch で名前解決できず、本文を直接読めなかった（セッションのネットワーク許可外とみられる）。公式ページの内容は WebSearch の要約経由でしか見ていない。そのため下記の「確認済み」は最小限にし、公式ページ経由のものも原則「報告あり」に落としている。
- Instagram の動画本体・再生数はログイン必須で取得不可。個別アカウントの実数値は「取得不可」。
- 根拠の強さ: 確認済み = 公式を直接確認 / 報告あり = 二次情報 / 推測 = 自分の推論。

## 1. 調査の目的と範囲
題材未定のため、Reelsで伸びる型・領域、AI生成動画の受容状況、AI開示ルール、アルゴリズム変化、推奨仕様を調べ、推奨領域を1つ選ぶ。台本は書かない。

## 2. 流行している型・フォーマット（5個）
一般Reels全体の傾向であり、AI動画に限った型ではない。いずれも二次情報（マーケ系ブログ中心）で、2026年11月時点の実測データは取得不可。

1. **繰り返せるフォーマット化（UGC風トーク、リスト解説、ビフォーアフター）**。報告あり。invideo、podcastvideos(2026-09) など。https://invideo.io/blog/instagram-reels-guide/ / https://www.podcastvideos.com/instagram-reels-2026-repeatable-formats/
2. **POVミニスキット、ニュース見出しの再現**。報告あり。podcastvideos（2026-09）。AI動画のミニドラマと相性が良いと推測。
3. **強いフック＋高速カット**（冒頭2秒、30秒で8〜15カット）。報告あり（ManyChat）。具体数値は単一ブログのため参考扱い。https://manychat.com/blog/instagram-trends-for-creators-2026/
4. **テキスト主体・引用・ランキング・スプリットスクリーン**。報告あり（MEAN CEO 2026-11）。https://blog.mean.ceo/instagram-trends-november-2026/
5. **AI生成の動物（猫・ペット）ショート**。報告あり。Tom's GuideがReels/TikTok/Shortsでの拡散を報道。Picsartは「猫忍者」リールが300万再生・16.8万いいねと紹介（単一の二次情報、Instagram上の実数は取得不可）。SCMPは中国のAIペットドラマが1億再生超と報じたが、Instagramの話ではない。https://www.tomsguide.com/ai/ai-image-video/ai-cat-videos-are-suddenly-everywhere-heres-why-the-internet-cant-stop-watching / https://picsart.com/blog/ai-cat-ninja-video-trend/ / https://www.scmp.com/news/people-culture/article/3313925/chinas-ai-generated-pet-dramas-take-internet-storm-one-amassing-100-million-views

## 3. 候補領域の比較（探索モード手順1〜4）
評価は推測（AI動画の一般的な得手不得手に基づく）。◎良 ○可 △難

| 領域 | 破綻しにくさ | 制作コスト | 量産性 | Reelsでの需要の根拠 | 備考 |
|---|---|---|---|---|---|
| A. 動物・非人間キャラの短尺スキット | ○（単体は良好、複数・接触は崩れやすい。Kapwing比較） | ○ | ◎ | 報告あり（上記5） | 人物ペルソナ規定を避けやすい（要確認） |
| B. 雑学・解説（AI映像＋ナレーション） | ◎（抽象カット中心） | ◎ | ◎ | 報告あり（リスト解説は定番） | AI音声は開示対象になりうる |
| C. 商品紹介・広告風 | △（形状・ロゴが崩れる） | ○ | ○ | 報告あり | 音源は商用制限に注意 |
| D. 人物キャラの日常・AIインフルエンサー | △ | △ | ○ | 取得不可 | 「AI生成プロフィール」ラベル必須（下記4） |
| E. ミニドラマ（人物中心） | △（一貫性） | △ | △ | 報告あり（POVスキット） | 人物の一貫性が難所 |
| F. ブレインロット/クリープパスタ系 | ◎ | ◎ | ◎ | 報告あり（404 Media） | 推奨しない（下記5） |

有望上位3: A、B、E寄りのPOVスキット。軽い深掘りの結果、E（人物）は一貫性とラベル規定の負担が大きいので、AとBを比較して推奨はA。

## 4. Instagram上でのAI動画の受容と規則

### 4-1. AI開示・ラベル
- **投稿単位**: Metaは、写実的な動画や写実的な合成音声をデジタル生成・改変した場合の開示を求め、未開示には罰則がありうるとされる。技術シグナルがあれば自動で「AI info」が付く。漫画風の風景動画などは対象外とする例がある。報告あり（公式ヘルプの検索要約。本文未確認）。https://help.instagram.com/761121959519495
  - 自動ラベルが付かなくても開示義務はなくならない、という記述あり。報告あり。
- **プロフィール単位（2026年8月31日）**: 「AI creator」ラベルを「AI-generated profile」に改称。AI生成の人物を前面に出すアカウントがラベルを付けないと、フォロワー以外への推薦（Explore/Reels等）が制限される。AIツールを使うだけの作成者は対象外。ラベルを付けても到達は下がらないとの報道。報告あり（TechCrunch 2026-08-31、Engadget、9to5Google、Digital Trends等）。公式本文は取得不可。
  - 「人物」の範囲（動物キャラ、擬人化、アニメ調が該当するか）は未確認。取得不可。
  - https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/ / https://9to5google.com/2026/08/31/instagram-ai-generated-influencers-label-update/ / https://engadget.com/2246914/instagram-will-demote-ai-generated-influencers-if-they-dont-clearly-label-their-account/

### 4-2. 受容・反応・炎上
- Mosseriは2025年末の発信で「AIが当たり前になり、偽物より本物に指紋を付ける方が現実的」と述べた。2026年は「生々しい人間らしさ」が有利になる論調。報告あり（Engadget、Tubefilter 2026-01-06）。https://www.engadget.com/social-media/instagram-chief-ai-is-so-ubiquitous-it-will-be-more-practical-to-fingerprint-real-media-than-fake-media-202620080.html
- クリエイターから「AIスロップ対策が不十分」との批判。報告あり（Futurism、Hello Partner）。2026年10月のFuturismは、AIでコメディアンのネタを盗用した偽コメディアン動画が拡散していると報じた（報告あり、一次未確認）。
- ブレインロットやクリープパスタ系AIリールが収益化されている問題を404 Mediaが調査。1本620万再生の例（二次報道）。報告あり。https://404media.co/brainrot-ai-on-instagram-is-monetizing-the-most-fucked-up-things-you-can-imagine-and-lots-you-cant
- PetaPixel（2026-09-01）は「人はAIクリエイターに騙されるのを嫌う」と論評。https://petapixel.com/2026/09/01/instagram-is-waking-up-to-the-fact-that-people-dont-like-being-tricked-by-ai-creators/
- 先行AIアカウントの具体名・実数値: 取得不可（ログイン必須。人間による提供を依頼）。

### 4-3. 音源・商用
- Instagramのライセンス音源は個人の非商用利用が前提。一部のビジネスアカウントや投稿タイプではライブラリが使えない。代替としてMetaのSound Collection（商用可）。報告あり（公式ヘルプ https://help.instagram.com/ipad-app/402084904469945 の検索要約、Adobeのガイド）。トラック数「約1.4万」は音楽ベンダー情報で未検証。
- 他アプリへの転載時、Instagram音源は対象外。報告あり（ベンダー情報）。
- 流行音源は、プロアカウントの「トレンド音源」タブで確認するのが現実的（ManyChat）。今回は取得不可。TikTok専用ツールは使っていない。

## 5. アルゴリズム/おすすめの変化
- **2026-04-30 オリジナル性の拡張**: 他者作品を主に再投稿し、意味ある加工をしない作成者は、非フォロワーへのおすすめから外れる。対象はReelsから写真・カルーセルに拡大。元投稿が再投稿より優先表示される。報告あり（PetaPixel 2026-04-30、TechCrunch、Engadget）。Instagram公式クリエイターページに同趣旨の記述（検索要約）: https://creators.instagram.com/recommendations-and-originality
- **推薦の適格条件**: オリジナルで、ガイドライン順守、可視透かしなし。透かし付き（特にTikTok）は不利。報告あり（公式クリエイターページの検索要約）。https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators
- ランキング主要信号は視聴時間、いいね率、送信（DM）率（2025年1月のMosseri発言として広く引用）。報告あり。
- 2026年6月に「Your Algorithm」をメインフィードへ拡張。2026年8〜9月に確認できる大きなランキング変更はなし（SocialPilot）。単一の二次情報。
- 「DM送信は3〜5倍の重み」「10本以上再投稿で除外」のような数値は出典不明。不採用。
- トライアルリール（2024-12開始）: 非フォロワーにのみ表示してテストできる。報告あり（PetaPixel 2024-12-13）。AI動画の反応見極めに使える（推測）。
- 影響の整理（推測）: AI動画でも一次制作＋独自編集であればオリジナル扱いになるはず。ただし他人のAI動画の転載、TikTok透かし付き素材は避ける。

## 6. 避けるべき点
- AI生成の人物を主役にしたアカウントで「AI-generated profile」ラベル未設定（到達制限）。
- 写実的なAI動画・AI音声を開示せずに投稿（罰則の可能性）。実在人物の肖像・声の模倣、実在コメディアンのネタの流用。
- ブレインロット/グロ/災害便乗系のAIスロップ。収益化されているが批判の的で、ブランドリスクが高い。
- 他アプリの透かし付き素材、他者動画の再投稿。
- 商用アカウントでの個人向けライセンス音源の使用。音源は無音で書き出し、Sound Collectionか自前音源を使うのが安全。
- 他社の著作物キャラ、有名人のそっくり生成。

## 7. 推奨仕様（Reels）— platform-specs の「要確認」欄への反映案
公式ページ本文は取得できず、検索要約経由のため、確認済みは0件。

| 項目 | 内容 | 強さ | 出典 / 日付 |
|---|---|---|---|
| 比率・解像度 | 9:16、1080x1920 | 報告あり（多数一致） | https://postfa.st/sizes/instagram/reels （2026-11-20確認） |
| 最大尺 | 3分（2025-01に90秒から拡大、Mosseriが発表） | 報告あり | https://www.socialmediatoday.com/news/instagram-officially-expands-reels-length-to-3-minutes/737766/ ほか（2025-01-20頃） |
| アプリ内撮影の既定 | 30秒、設定で3分に変更可 | 報告あり | Kapwing解説 |
| カバー | 公式ヘルプは420x654 px（約1:1.55）を推奨、投稿後の変更不可と報告 | 報告あり（公式ヘルプの検索要約） | https://help.instagram.com/1038071743007909 （2026-11-20確認、本文未読） |
| グリッド表示 | プロフィールは3:4表示（2025-01〜）。1080x1920は上下約240pxが切れる。比率の数値は公式未確認 | 報告あり（コミュニティ計測） | https://postfa.st/sizes/instagram/reels ほか |
| フィード内プレビュー | 4:5で表示されることが多い | 報告あり | 同上 |
| テキスト安全域 | 1080x1920で上から約285〜1250px内（ベンダー提案、公式値ではない） | 推測（ベンダー推奨） | https://www.revid.ai/instagram-reels-safe-zone |
| キャプション | 最大2200文字（絵文字は2文字換算の説明あり）。「続きを読む」前に見えるのは冒頭のみ（長さの数値は情報源で不一致） | 報告あり | https://growthscribe.com/instagram-caption-character-limit/ ほか（2026-11-20確認） |
| ハッシュタグ | 2025-12に1投稿5個までへ制限と報道。30個と書く古い情報と競合 | 報告あり（未確認・競合あり） | https://www.businesstoday.in/technology/news/story/no-more-hashtag-stuffing-instagram-limits-hashtag-usage-to-just-5-per-reel-and-post-507444-2025-12-19 |
| AI開示 | 写実的な生成動画・音声は開示。自動「AI info」あり。プロフィールは「AI-generated profile」 | 報告あり | 上記4-1 |
| 音源の商用制限 | ライセンス音源は個人非商用が前提。事業用はSound Collection | 報告あり | https://help.instagram.com/ipad-app/402084904469945 |
| Edits | アプリ書き出しは透かしなし、最長10分録画 | 報告あり | digitalcameraworld |

## 8. 企画への示唆（3行）
1. 推奨領域は A（動物・非人間キャラの短尺スキット/ループ）。破綻しにくい単体カット中心で量産でき、AI動物動画の拡散報道がある。次点はB（雑学・解説）。
2. 独自の編集・ナレーションを加えてオリジナル性を示し、写実的なら AI info 開示、人物キャラなら「AI-generated profile」を設定する。音源はSound Collectionか自前にする。
3. 最初はトライアルリールで反応を見て、冒頭2秒のフックと3:4グリッドでも読めるカバーを設計する。

## 9. 人間に手動で渡してほしい情報
- Instagramのリール上で、狙い目領域（AI動物スキット、AI雑学解説）の先行アカウントURLと、直近の再生数・いいね・コメント傾向のスクショ（各3件以上）。取得不可だったため。
- 自分のプロアカウントの「トレンド音源」タブのスクショ（日付入り）。
- 投稿画面の「AI開示」設定の文言と、プロフィール設定内の「AI-generated profile」ラベルの有無（スクショ）。
- help.instagram.com と techcrunch.com をネットワーク許可に追加してもらえれば、公式本文を直接確認して「確認済み」に引き上げられる。

## 10. 調べたクエリと採否
1. Instagram AI info label disclosure policy 2026: 採用（プロフィールラベル、投稿ラベル）
2. Reels algorithm update 2026 Mosseri original content: 採用（2026-04の変更）。ベンダー数値は不採用
3. Reels length / aspect ratio / cover: 採用（公式カバー値）。長さは競合のため追加検索
4. AI generated Reels backlash AI slop 2026: 採用（反応、炎上）
5. Reels trending formats November 2026: 参考扱い（マーケ系ブログ）
6. trial reels / Edits / caption limit: 一部採用。キャプションは不足のため再検索
7. licensed music business restrictions: 採用（公式ヘルプ要約）。ベンダーの数値は不採用
8. AI animal viral Reels: 採用（Instagram固有の実数値は取得不可）
9. Meta AI info label how to label: 採用
10. caption 2200 / hashtag 5: 採用（ハッシュタグは競合あり）
11. creators.instagram.com ranking originality: 採用
12. Mosseri authenticity AI 2026: 採用
13. Reels 3 minutes announcement / safe zone（2検索）: 採用。安全域はベンダー推奨のため参考扱い

## 付記: platform-specs への追記案
上記7の表を、日付（2026-11-20）と出典URL付きで追記できる。ただし確認済みは0件で、「報告あり」として追記すること。
