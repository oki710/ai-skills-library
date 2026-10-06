# Cursor向け設計

確認日：2026-10-07。利用者のCursorの版・契約・有効機能は未確認です。機能の利用可否を断定するときは、下記の公式資料と実際の環境を確認してください。

## 作業の入口

「Cursor向けに改善」はCursorへ渡す依頼文を作ってください。Cursorの起動や設定の書換えは含みません。「配置・更新」まで依頼された場合は既存の配置先・識別名・適用範囲を調べてから変更し、同名の別ファイルを代替更新しません。

| 状況 | 依頼文の設計 |
|---|---|
| 小さく明確な修正 | Agentで現状確認、最小修正、関連検証まで。長い計画や全テスト実行を一律に要求しない |
| 複数案・広い変更・不明な要件 | Plan Modeを候補にし、調査と計画の完成条件、実装を始める条件を明記する |
| 読み取り専用の調査 | 既存ログ・設定を根拠に仮説を分ける。Debug Modeによる計測追加も変更なので、勝手に含めない |
| レビューだけ | 問題箇所、影響、根拠、修正案を示す。実際の書換えはしない |

関連ファイルが分かれば`@`で指定し、不明ならAgentに検索させてください。未確認のパスを必須入力にせず、無関係な全ファイル・全ログを読み込ませません。受け入れ条件は実装方法だけでなく、期待する入力・出力・振る舞いで示してください。[1][2][3]

## 指示の配置

| 用途 | 配置と注意 |
|---|---|
| 今回の目的・入力・成功条件 | チャットへ。再利用の必要がなければ設定ファイルを増やさない |
| 個々の利用者の安定した文体 | User Rulesへ。案件固有の条件は混ぜない |
| プロジェクトやパスの規約 | `.cursor/rules/*.mdc`。`description`、`globs`、`alwaysApply`を用途に合わせる |
| 製品間で共有する規約 | `AGENTS.md`。既存の親子関係を保持する |
| 必要時に呼ぶ改善手順 | Agent Skill。本文を短くし、詳細は必要時に参照する |

Rulesは`.mdc`で渡し、すべてを常時適用にしないでください。ファイル指定、関連性に基づく選択、手動呼出しを区別します。手動コマンドをSkillへ移行するときは、手動限定の要件を保ち、対応を確認したうえで`disable-model-invocation: true`を使います。同名コマンドとの競合を確認し、元ファイルは依頼なく削除しません。[4][5]

## 最近の変化と使い分け

以下の製品機能を一律の前提にせず、案件と利用環境に合う場合だけ候補にしてください。

- **Skillsと文脈の分離**：再利用手順と常時規約を分け、必要な資料だけ読み込ませる構成にしてください。[4][5]
- **Custom Modes（2026-08-19の更新）**：同じSkillを継続して適用する必要がある場合だけ候補にしてください。単発の呼出しと区別します。[6]
- **Projects（2026-09-10の更新）**：長期案件で共有する決定事項・検証結果・残作業を短く維持する候補です。提供状況を確認し、通常のコードベースの規約と混同しません。[7]
- **Rollouts／Security Review（2026-09-23の更新）**：Teams／Enterprise向けの補助機能です。未契約でも既存CI・レビュー・監視で検証できる依頼にしてください。[8]

モデルは固定せず、ユーザーの指定と実際の選択肢を尊重してください。並列エージェントは作業を独立して分けられ、コストと統合負担に見合う場合だけ検討します。担当・変更範囲・完了条件を分け、定期実行、無制限のループ、MCP接続を無断で追加しません。

## 業務での境界

組織のルール、データ分類、権限・承認設定を守ってください。ログや設定は必要最小限のマスク済み入力を使い、秘密値を表示・公開検索・外部送信しません。プロンプトは技術的なアクセス制御の代わりにはなりません。

`.cursorignore`はターミナルやMCPを含む全面的なアクセス遮断ではありません。除外された情報を別ツールで迂回取得する指示を作らず、許可された資料で進めてください。[9]

## 公式資料

1. [Prompting agents](https://cursor.com/docs/agent/prompting)
2. [Plan Mode](https://cursor.com/docs/agent/plan-mode)
3. [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices)
4. [Rules](https://cursor.com/docs/rules)
5. [Agent Skills](https://cursor.com/docs/skills)
6. [Cloud Agents and Cursor Harness Improvements](https://cursor.com/changelog/08-19-26)
7. [Cursor Projects](https://cursor.com/changelog/projects)
8. [Rollouts and Security Review](https://cursor.com/changelog/rollouts-and-security-reviewer)
9. [Ignore file](https://cursor.com/docs/reference/ignore-file)
