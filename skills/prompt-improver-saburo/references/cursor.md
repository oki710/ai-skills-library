# Cursor向け設計

確認日: 2026-10-27。利用者のCursor版、契約、利用可能モデル、Cloud Agent機能は実行時に確認する。三郎はCursor機能を列挙するためではなく、**実装担当が迷わない作業契約を作るため**に使う。

## 三郎の役割

Cursor向けでは、三郎をCoordinator / Specification側として扱う。

1. 目的、現状、変更範囲、禁止範囲を短く整理する。
2. 受入条件を利用者から観測できる形にする。
3. 反復が必要なら Goal / Observe / Verify / Adjust / Stop を定める。
4. 実装担当へ渡す対象、根拠、権限、Verifierを明示する。
5. 実装そのものは、依頼が「改善して実行」でない限り始めない。

明確な小修正に長い計画や工程表を強制しない。広い変更、複数案、未確認要件がある場合のみPlan Modeを候補にする。

## Contextを小さく保つ

CursorのSkillsは `references/` を必要時に読み込める。SKILL.mdへ全原則を詰め込まず、対象に関係する資料だけ参照する。

- 関連ファイルが分かれば `@` や検索対象を絞る。
- 不明なパスを発明せず、Agentに検索させる。
- 大きいcontext windowが使えても、無関係な全ファイルを先に読ませない。
- 既存のRules、AGENTS.md、Skill、テスト手順を正本として優先する。

## Subagents

Subagentは、三郎が作る実行契約の中で **独立性がある作業** にだけ割り当てる候補とする。

向いている例:
- コードベース調査と公式仕様調査
- 複数の独立モジュールの読み取りレビュー
- 実装担当と、変更権限を持たない独立Verifier
- 複数案の比較

避ける例:
- 同じファイルを複数Agentが同時編集
- 前段の結果が必須な作業を無理に並列化
- 子Agentへ必要な受入条件や権限を渡さない

CursorはSubagentごとに独立contextを持つため長い調査を分離できる一方、coordination costもある。常時起動を要求せず、分割利益がある場合だけ使う。

## Hooks

format、secret scan、PII検査、危険な書込みのgateなど、毎回同じ判定が必要な条件はHooksやCIの候補にする。プロンプトの「注意して」で強制しない。

ただしHookの新規作成・変更は設定変更であり、三郎がCursor向けプロンプトを作るだけの依頼から勝手に追加しない。既存Hookがある場合は、その失敗を無視したり迂回したりしない。

## Projects

数週間以上にわたるfeature、migration、多数PRなど、単一チャットを超える作業ではProjectsを候補にできる。Projectsのcoordinatorは計画・委譲を担当し、実装はAgentへ渡すため、三郎の「仕様・受入条件・委譲境界」と相性がよい。

短い修正では使わない。Cloud Agentsや契約条件、Privacy Mode等で利用可否が変わるため、未確認の環境へ前提化しない。subscriptionや定期処理もユーザーが依頼した場合だけ設計する。

## Grok 4.7

2026-10-27時点でCursor公式はGrok 4.7を、難しく長時間のcoding / knowledge work向けモデルとして案内している。Grok 4.7が実際に選択されている場合は:

- 内部思考順序を細かく縛るより、Goal、制約、受入条件、Verifier、Stopを明確にする。
- 自己検証だけに頼らず、テスト、lint、build、型検査、実測など外部Verifierへ接続する。
- 長いcontextを使えることを理由に、無関係な資料を全部投入しない。
- 長時間作業では、決定事項、検証済み、未解決、次の一手を短い状態として引き継ぐ。

モデル指定がなければGrok 4.7を強制しない。effort、速度、料金、提供プランをプロンプトへ固定せず、必要なら実行時の公式情報とUIで確認する。

## 公式資料

- [Agent Skills](https://cursor.com/docs/skills)
- [Subagents](https://cursor.com/docs/subagents)
- [Hooks](https://cursor.com/docs/hooks)
- [Projects](https://cursor.com/docs/agent/projects)
- [Grok 4.7](https://prod.cursor.com/help/models-and-usage/grok-4-7)
- [Improved token efficiency for longer agent runs](https://cursor.com/blog/improved-token-efficiency)
