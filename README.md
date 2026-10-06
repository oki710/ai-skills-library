# AI Skills Library

[![Validate skills](https://github.com/oki710/ai-skills-library/actions/workflows/validate.yml/badge.svg)](https://github.com/oki710/ai-skills-library/actions/workflows/validate.yml)

複数のAIエージェントで再利用できる、公開向けのAgent Skillsライブラリです。各スキルは、YAML frontmatter付きの `SKILL.md` として管理します。

このリポジトリには、個人情報、秘密情報、組織や家庭の環境に固有のホスト名・IPアドレス・パスを含めません。

## 収録スキル

| スキル | 用途 |
|---|---|
| [`japanese-text-editor`（添削次郎）](skills/japanese-text-editor/SKILL.md) | 意味・条件・トーンを保って日本語を添削する。[Cursorでの使い方](docs/cursor-tensaku-jiro.md) |
| [`prompt-optimizer`](skills/prompt-optimizer/SKILL.md)（プロンプト改善太郎） | LLM・Cursor向けの依頼を、目的・制約・検証が明確なプロンプトへ改善する |
| [`infrastructure-change-reviewer`](skills/infrastructure-change-reviewer/SKILL.md) | インフラ変更案の影響、前提、ロールバック、検証方法を確認する |

## 使い方

### Cursorでプロンプト改善太郎を使う

`skills/prompt-optimizer/` をフォルダーごと、作業プロジェクトの `.cursor/skills/prompt-optimizer/` へ配置します。Agentの `/` メニューから `prompt-optimizer` を選び、改善したい原案を渡してください。

[Cursor向けの導入手順・使用例・確認範囲](docs/cursor-prompt-optimizer.md)を参照してください。2026-10-07の公式情報を反映しています。配布版の構造と内容を検証し、Cursor実機での動作確認は未実施です。

### 1. リポジトリを取得する

```sh
git clone https://github.com/oki710/ai-skills-library.git
cd ai-skills-library
```

### 2. 必要なスキルを共通パスへコピーする

このリポジトリの `skills/` は配布用の正本です。CodexとGemini CLIの共通パスとして使える `.agents/skills/` へ、必要なスキルだけをコピーします。

macOS / Linux:

```sh
mkdir -p ~/.agents/skills
cp -R skills/japanese-text-editor ~/.agents/skills/
```

Windows PowerShell:

```powershell
$userProfile = [Environment]::GetFolderPath('UserProfile')
New-Item -ItemType Directory -Force "$userProfile\.agents\skills" | Out-Null
Copy-Item -Recurse skills\japanese-text-editor "$userProfile\.agents\skills\"
```

ほかの配置方法と対応範囲は、[互換性ガイド](docs/compatibility.md)をご覧ください。

### Cursorで添削次郎を使う

[導入ガイド](docs/cursor-tensaku-jiro.md)から、Skill版または手動Rule版を選べます。2026-10-07にCursor公式資料を再確認し、必要時の呼び出し、継続添削用Custom Mode、対象範囲の限定に対応しています。Cursor実機での動作は未検証です。

## 新しいスキルを作る

1. [`templates/skill-template`](templates/skill-template/SKILL.md) を `skills/<skill-name>/` へコピーします。
2. フォルダ名とfrontmatterの `name` を同じ名前へ変更します。
3. `description` に、スキルの用途と呼び出す場面を書きます。
4. 本文に必要な手順、制約、出力形式、例を記載します。
5. 検証を実行します。

スキル名は、英小文字、数字、ハイフンだけを使います。詳細は[コントリビューションガイド](CONTRIBUTING.md)をご覧ください。

## 検証

Python 3.10以降を使用します。外部パッケージは不要です。

```sh
python scripts/validate_skills.py skills templates/skill-template
python -m unittest discover -s tests -v
```

検証では、必須frontmatter、名前、フォルダ名との一致、descriptionの長さ、本文の有無を確認します。同じ検証は、pushとpull requestのGitHub Actionsでも実行されます。

## 公開時の安全ルール

- トークン、APIキー、パスワード、秘密鍵をコミットしません。
- 実在する内部ホスト名、IPアドレス、アカウント、個人用パスを例に使いません。
- 公開できない運用手順を、値だけ伏せて転載しません。
- 汎用化できる判断方法だけを公開し、環境固有の設定はprivateリポジトリで管理します。

脆弱性や秘密情報の混入を見つけた場合は、公開Issueを作成せず、[SECURITY.md](SECURITY.md)に従ってください。

## ライセンス

[MIT License](LICENSE)です。
