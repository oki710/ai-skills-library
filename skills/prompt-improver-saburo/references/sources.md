# 出典と併用

調査日: 2026-10-27。以下は判断の参考資料であり、三郎の性能や規格適合を保証するものではない。文章・コードの転載は行わず、用途に合わせて独自の手順として構成した。最新仕様が関わる作業では利用時に公式資料を再確認する。

| 資料 | 確認した内容と三郎での扱い |
| --- | --- |
| [yomiyasu v1.1.2](https://github.com/nanaism/yomiyasu/releases/tag/v1.1.2) / [対象版のSKILL](https://github.com/nanaism/yomiyasu/blob/v1.1.2/skills/yomiyasu/SKILL.md) / [作者の解説](https://zenn.dev/algoartis/articles/0b1c731881b25c) | 意味と文の働きを保持し、変更前後を点検する設計を参照。三郎では要求・禁止・仮定・権限の保持へ応用。日本語推敲そのものの優劣は比較していない |
| [GitHub Spec Kit](https://github.com/github/spec-kit) / [SDDの説明](https://github.com/github/spec-kit/blob/main/spec-driven.md) | 要求、計画、作業、検証を結びつける考え方を参照。三郎では小変更に仕様書一式の生成を強制せず、既存コードとの整合を重視 |
| [Superpowers](https://github.com/obra/superpowers) / [systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 設計、原因調査、実装、検証の分離を参照。三郎では全件TDD、テスト前に書いたコードの削除、常時の委譲を必須にしない。緊急緩和と根本修正を区別 |
| [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | 設計、複雑さ、機能、妥当なテスト、命名、文書を確認。要求されていない一般化を避け、テスト自体の有効性もレビュー |
| [NIST SSDF](https://csrc.nist.gov/Projects/ssdf) | SDLCへセキュリティ実践を組み込み、リスクや費用に応じて選択する方針を参照。項目を全部並べる方式にしない。全規格への準拠判定は行っていない |
| [OWASP ASVS](https://owasp.org/projects/asvs) | アプリケーションの技術的セキュリティ要件と検証の参照先。具体的な要件IDを使う場合は版と本文を確認。三郎のみでASVS適合とはしない |
| [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) | テストを責務と境界に合わせて選ぶ参考。件数や層の比率を固定せず、変更のリスクから選択 |
| [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) | 過負荷時の再試行に上限とバックオフ等が必要な背景を参照。具体値や再試行対象はサービス仕様に合わせる |
| [Agent Skills仕様](https://agentskills.io/specification) | SKILL.mdと必要時に読む参照資料を分離。形式の可搬性と、実行ツール・権限・配置の互換性は区別 |
| [Cursor Agent Skills](https://cursor.com/docs/skills) | `references/` の段階的読込み、`paths`、手動呼出し、Custom Modeの現行仕様を確認。Skill本文を肥大化させず必要時に詳細を読む設計へ反映 |
| [Cursor Subagents](https://cursor.com/docs/subagents) / [longer agent runs](https://cursor.com/blog/improved-token-efficiency) | 独立コンテキストと並列化の利点、およびcoordination costを確認。三郎では常時委譲を要求せず、独立性がある場合だけ分割を設計 |
| [Cursor Hooks](https://cursor.com/docs/hooks) | formatter、secret/PII scan、危険操作のgateなど決定的な検査に利用可能。プロンプト上の注意だけで強制せず、Hook作成自体は設定変更として扱う |
| [Cursor Projects](https://cursor.com/docs/agent/projects) | 長期案件でcoordinatorが実装を委譲し共有状態を維持する仕組みを確認。短い作業や利用不可プランへ前提化しない |
| [Cursor Grok 4.7](https://prod.cursor.com/help/models-and-usage/grok-4-7) | 難しい長時間coding、長いcontext、自己検証が強い現行flagshipとして確認。モデル固定はせず、選択済みの場合に成果条件とVerifierを明確にする設計へ反映 |
| [SWEBOK公開案内](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | 検索で公式公開案内を確認。直接取得は403で、本文全体は未精読。網羅性や準拠の根拠として使わない |

## 併用先の選び方

日本語の仕様書やPR説明文を整えるなら **yomiyasu**。工程をまとめて支援する既存スキル群なら **Superpowers**。チームで仕様と実装計画を継続管理するなら **Spec Kit** が候補となる。Spec Kitは単一のスキルではなく開発ツールキットである。

複数の工程管理スキルを同時に主担当にすると、承認や出力が重複することがある。三郎で要求を整理した後、実行は開発実行四郎か別の工程管理方式のどちらを主にするか決める。yomiyasuは文章の仕上げに限定すると役割を分けやすい。第三者スキルを勝手にインストール・更新しない。

太郎は幅広い依頼の改善、三郎は開発・改修に特化した具体化を担当する。同じ本文を両方で何度も改善して情報を増やさない。利用環境が違う場合は、その環境の現在のスキル・権限・公式仕様を確認する。
