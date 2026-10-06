# 添削次郎をCursorで使う

最終確認日: 2026-10-07

メール、Slack、業務文書、READMEの文章を、意味・条件・トーンを保って整える汎用の日本語添削ツールです。個人や会社の設定、原稿、会話履歴、実在する内部環境の値は収録していません。特定のモデルに固定せず、リポジトリの[MIT License](../LICENSE)で利用・改変できます。

## 使い方を選ぶ

| 用途 | 配布物 | 配置先・呼び出し |
| --- | --- | --- |
| 単発の添削、繰り返す文章編集 | [Skill](../skills/japanese-text-editor/SKILL.md) | `.cursor/skills/japanese-text-editor/SKILL.md` に配置し、`/japanese-text-editor` を選ぶ |
| 毎回明示して使うRules運用 | [手動Rule](../cursor/rules/tensaku-jiro.mdc) | `.cursor/rules/tensaku-jiro.mdc` に配置し、`@tensaku-jiro` を選ぶ |

どちらか一方を導入してください。同じ依頼で両方を読み込む必要はありません。

### Skillを使う

1. 配布用の `skills/japanese-text-editor/` フォルダを、対象プロジェクトの `.cursor/skills/` へコピーします。同名の既存ファイルがある場合は、差分を確認してから更新します。
2. Cursorで対象プロジェクトを開き、`/` の候補から `japanese-text-editor` を選びます。追加直後に表示されなければ、プロジェクトを開き直して検出を確認します。
3. 添削する原稿を貼り付けるか、対象ファイルと範囲を指定します。
4. 複数の原稿を続けて扱うときは、対応画面でスキルの `Use as Mode` を選べます。公式資料ではCustom Modesの提供先をAgents WindowとCLIとしています。

Skillsは依頼内容に応じた自動選択にも対応します。手動呼び出しだけに限定したい場合は、Cursor用に配置したコピーのfrontmatterへ `disable-model-invocation: true` を追加できます。これはCursor固有の設定なので、共通の正本には追加していません。

Cursorは `.agents/skills/` も読み込みますが、同じスキルを両方に重複配置しないでください。プロジェクト内で共有する場合は配置先を1つ決めます。

### Ruleを使う

1. `cursor/rules/tensaku-jiro.mdc` を、対象プロジェクトの `.cursor/rules/tensaku-jiro.mdc` へコピーします。
2. チャットの `@` 候補から `tensaku-jiro` を選んで原稿を渡します。

このRuleは `alwaysApply: false` だけを指定し、`description` と `globs` を設定していません。公式仕様上、手動で指定した場合だけ適用される構成です。既存の `AGENTS.md` や他のルール全体を置き換える必要はありません。

このリポジトリはファイルをコピーする配布方式です。Cursor Marketplaceのインポート用パッケージは含みません。

## 依頼例

いずれも架空の短文です。送信先や原稿は実際の用途に合わせて渡してください。

**Slack向け・標準**

```text
/japanese-text-editor
同僚向けのSlackです。標準で添削し、完成文だけ返してください。

明日14時から作業をする予定です。停止時間は最大15分の見込みですが、
まだ確定していません。完了したら連絡します。
```

**ファイルの一部へ反映**

```text
/japanese-text-editor
指定した文書の「概要」セクションだけを軽微に添削して反映してください。
コードブロック、リンク先、数値、ほかのセクションは保持してください。
```

**評価だけ**

```text
/japanese-text-editor
次の文章の曖昧さだけを指摘してください。全文リライトは不要です。

承認された場合だけ、翌営業日に対応します。
```

Ruleを使う場合は、例の `/japanese-text-editor` を `@tensaku-jiro` に置き換え、候補から実際に選択します。

## 今回反映した設計

- 必要なときに呼び出すSkills／手動Rulesと、継続作業のCustom Modeを使い分ける。
- 原稿、選択範囲、参考資料、ファイルへの反映指示を分離する。
- 意味・否定・例外・数値・不確実さ・責任範囲・トーンを保持する。原稿にない謝罪・約束・期限を補わない。
- 原稿内の命令は編集対象として扱い、操作の権限にしない。
- 事実確認を行った場合と、文章だけを整えた場合を区別する。無関係な検索や過剰な検証を増やさない。

新機能の存在を理由に、文章添削へ自動実行・外部送信・複数エージェントを追加していません。仕事に必要な対象指定と見直しに集中する設計です。

## 業務利用と検証範囲

この配布物に個人情報や社内原稿は含みません。利用時に渡す業務原稿の取り扱いは、勤務先のAI利用規定と承認されたCursor環境に従ってください。指示文だけでデータの送信先や保存設定を制御できるものではありません。

公開前に、frontmatterと既存の検証スクリプト、架空の文章を使った応答、Markdownの部分編集を確認しています。Cursor実機での検出・表示・モデルごとの品質は未検証です。確認用の短文から試してください。

## 公式資料

- [Rules](https://cursor.com/docs/rules): `.mdc`、適用条件、短く用途を限定したルール。
- [Agent Skills](https://cursor.com/docs/skills): 配置先、手動呼び出し、必要時の読み込み、Cursor固有の設定。
- [Prompting agents](https://cursor.com/docs/agent/prompting): 対象コンテキストの指定、Custom Modesの利用先。
- [Changelog](https://cursor.com/changelog): 2026-08-19のCustom Modesに関する案内を確認。

## 更新時

編集指示の正本は `skills/japanese-text-editor/SKILL.md` です。Rule版には同じ本文を収録しています。正本を変更した際はRuleの本文も同期し、機能や制約が分岐していないことを確認してください。製品仕様は再確認日と公式リンクを更新し、未検証の動作を確認済みと記載しないでください。
