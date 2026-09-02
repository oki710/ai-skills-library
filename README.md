# AI Skills Library

[![Validate skills](https://github.com/oki710/ai-skills-library/actions/workflows/validate.yml/badge.svg)](https://github.com/oki710/ai-skills-library/actions/workflows/validate.yml)

複数のAIエージェントで再利用できる、公開向けのAgent Skillsライブラリです。各スキルは、YAML frontmatter付きの `SKILL.md` として管理します。

このリポジトリには、個人情報、秘密情報、組織や家庭の環境に固有のホスト名・IPアドレス・パスを含めません。

## 収録スキル

| スキル | 用途 |
|---|---|
| [`japanese-text-editor`](skills/japanese-text-editor/SKILL.md) | 事実と意味を保ちながら、日本語の文章を校正・校閲する |
| [`prompt-optimizer`](skills/prompt-optimizer/SKILL.md) | LLM向けの指示を、明確で再利用可能なプロンプトへ改善する |
| [`infrastructure-change-reviewer`](skills/infrastructure-change-reviewer/SKILL.md) | インフラ変更案の影響、前提、ロールバック、検証方法を確認する |

## 使い方

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
