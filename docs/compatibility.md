# 互換性ガイド

このリポジトリは、[Agent Skills仕様](https://agentskills.io/specification)に沿った `SKILL.md` を配布します。確認日は2026年9月2日です。

## 共通形式

各スキルは、次の構成です。

```text
skill-name/
├── SKILL.md
├── scripts/       # 必要な場合だけ
├── references/    # 必要な場合だけ
└── assets/        # 必要な場合だけ
```

`SKILL.md` の先頭には、少なくとも `name` と `description` が必要です。`name` は親フォルダ名と一致させます。

## 対応状況

| 製品 | 配置先 | このリポジトリでの扱い |
|---|---|---|
| ChatGPTデスクトップ内のCodex / Codex CLI / IDE拡張 | リポジトリまたはユーザーの `.agents/skills/` | 対応 |
| ChatGPTのChat / Work | スタンドアロンスキルまたはプラグイン | ソースとして対応。配布用パッケージは未収録 |
| Gemini CLI | `.gemini/skills/` または `.agents/skills/` | 対応 |
| その他のAgent Skills対応製品 | 製品の指定するskillsフォルダ | 仕様互換。実行前に各製品の資料を確認 |

このリポジトリ内の `skills/` は、配布とレビューのための正本です。製品が自動検出する場所ではないため、必要なスキルを製品のskillsフォルダへコピーまたはリンクしてください。

## ChatGPT / Codex

[OpenAIの公式資料](https://learn.chatgpt.com/docs/build-skills)では、Codexがリポジトリ内とユーザー領域の `.agents/skills/` を読み込みます。スキルは明示的な指定、または `description` と依頼内容の一致によって選ばれます。

配置例:

```text
<repository>/.agents/skills/japanese-text-editor/SKILL.md
<user-home>/.agents/skills/japanese-text-editor/SKILL.md
```

Webやモバイルを含む広い配布には、OpenAIはプラグインとしてのパッケージ化を案内しています。このリポジトリは、現時点では単体スキルのソースライブラリです。

## Gemini CLI

[Gemini CLIの公式資料](https://geminicli.com/docs/cli/skills/)では、標準の `.gemini/skills/` に加えて `.agents/skills/` エイリアスに対応しています。

配置例:

```text
<repository>/.agents/skills/japanese-text-editor/SKILL.md
<user-home>/.agents/skills/japanese-text-editor/SKILL.md
```

対話セッションでは `/skills list` で検出状況を確認できます。追加したスキルが表示されない場合は `/skills reload` を実行します。ワークスペース内のスキルを使うには、そのフォルダが信頼済みである必要があります。

## 互換性の範囲

このリポジトリの検証は、ファイル構造とfrontmatterを対象とします。各製品での自動選択、使用できるツール、権限、確認画面は製品ごとに異なります。公開前には、対象製品で実際の依頼を使って動作を確認してください。

特定製品だけが使うfrontmatterは、共通スキルへ安易に追加しません。追加する場合は、その製品以外での扱いを確認し、この文書へ制約を追記します。
