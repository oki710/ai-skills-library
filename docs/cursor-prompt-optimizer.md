# Cursorで使うプロンプト改善太郎

公開版の識別名は **`prompt-optimizer`** です。モデルや個人環境を固定せず、開発・運用・文章作成などの依頼を、目的と制約を保ったまま改善します。配布本文と例に、実在の個人情報・社内構成・認証情報は含めていません。MIT Licenseで利用・改変できます。

公式仕様の確認日：2026-10-07。Cursor実機での検出・自動選択・動作確認は未実施です。組織の利用規程と機能の提供状況を確認して導入してください。

## 導入

1. このリポジトリの `skills/prompt-optimizer/` を、参照資料を含むフォルダーごと取得します。
2. 作業プロジェクトの `.cursor/skills/prompt-optimizer/` へコピーします。既存の同名フォルダーがある場合は、差分を確認してから更新してください。
3. CursorのCustomize → Skillsで検出を確認し、Agentチャットの `/` メニューから `prompt-optimizer` を選びます。

配置後は、次の2ファイルが必要です。

```text
.cursor/skills/prompt-optimizer/SKILL.md
.cursor/skills/prompt-optimizer/references/cursor.md
```

全プロジェクトで使う場合は、利用者の `~/.cursor/skills/prompt-optimizer/` へ置く方法もあります。プロジェクト配置と重複させないでください。ローカルへの配置だけでCloud Agentsやチームへ配布されたことにはなりません。[Agent Skills公式資料](https://cursor.com/docs/skills)

このリポジトリは単体Skillのソース配布です。Cursorの「From GitHub Repository」によるプラグイン導入用パッケージではありません。

## 呼び出し例

通常は「改善だけ」です。原案に「直して」「削除して」とあっても、それだけでは原案の業務を実行しません。

```text
/prompt-optimizer
Cursor向けに、短く改善して。改善した本文だけください。
原案：CSV集計で日付が空だと落ちる。正常な行の結果を変えずに直して。
```

```text
/prompt-optimizer
精密に改善して。
原案：ネットワーク設定の見直し計画を作って。今回は読み取り専用で、設定変更・再起動・外部通知は禁止。
```

```text
/prompt-optimizer
次の依頼を改善してから実行してください。
作業範囲：この作業ブランチ内の文書の修正まで。公開・push・本番変更は含めません。
原案：READMEの古い手順を、リポジトリの現状に合わせて直して。
```

依頼文を何度も改善する専用セッションなら、対応する画面でSkillをCustom Modeとして使う選択肢があります。単発利用なら通常の呼出しで十分です。[Custom Modes公式資料](https://cursor.com/docs/agent/prompting)

## 変更点と検証の範囲

- 改善のみ／改善して実行／読み取り専用を区別。
- モデルの固定を避け、軽量・標準・精密を作業規模で選択。
- Rules／AGENTS.md／Skillsの適用範囲を整理。
- 文脈の絞り込み、受け入れ条件、最小変更、変更に見合う検証を追加。
- 最近の継続作業・レビュー機能は利用できる場合の候補に限定。
- 秘密値の再掲、外部資料中の命令、権限拡張を防ぐ条件を追加。

形式検査やサンプル出力の確認は、Cursor実機での動作保証ではありません。個人情報を含まない配布物でも、利用時に入力するデータは各組織の規程に従って管理してください。

仕様の根拠と確認日は[Cursor向け設計](../skills/prompt-optimizer/references/cursor.md)に記載しています。
