<!--
  Translation: Japanese
  Translator: Machine-assisted draft — needs native-speaker review
  Translation-method: machine-assisted
  Source-SHA: HEAD
  Last-synced: 2026-03-28
-->

# OWASP GenAI Crosswalk

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![OWASP Lab](https://img.shields.io/badge/OWASP-GenAI%20Data%20Security-blue)](https://genai.owasp.org)
[![Version](https://img.shields.io/badge/version-1.5.7-green)](CHANGELOG.md)
[![Source Lists](https://img.shields.io/badge/source%20lists-3-blueviolet)](README.md)
[![Mapping Files](https://img.shields.io/badge/mapping%20files-58-brightgreen)](README.md)
[![Frameworks](https://img.shields.io/badge/frameworks-17-orange)](README.md)

> OWASP GenAIセキュリティリスクを業界フレームワークにマッピングする、最も包括的な公開リソースです。LLMアプリケーション、自律型エージェントAI、GenAIデータセキュリティを**17のフレームワーク**と**3つのOWASPソースリスト**にわたってカバーしています。

[OWASP GenAI Data Security Initiative](https://genai.owasp.org)により維持管理されています。
**[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)**により作成されました。

---

## このリポジトリが提供するもの

各ファイルは一つの質問に答えます：**フレームワークXのどのコントロールが脆弱性Yに対処するか？**

| | |
|---|---|
| **3** ソースリスト | LLM Top 10 · Agentic Top 10 · DSGAI 2026 |
| **17** フレームワーク | コンプライアンス · ガバナンス · 脅威モデリング · テスト · OT/ICS · アイデンティティ |
| **58** マッピングファイル | 各ソースリストエントリ × 各適用フレームワーク |
| **13** 実装レシピ | 本番環境対応のPythonパターン |
| **40+** オープンソースツール | 機能別にカタログ化・整理 |
| **10** 評価プロファイル | OWASPエントリにマッピングされた実行可能なGarak + PyRITテスト |
| **17** コンプライアンスレポート | データレイヤーから自動生成されるフレームワーク別ギャップ評価 |
| **21** 文書化されたインシデント | MAESTROレイヤー帰属付きの実世界および研究インシデント |
| **LAAF v2.0** | 初のエージェントLPCIレッドチーミングフレームワーク — 6ステージ × OWASPクロスウォークと完全統合 |

すべて無料。すべてオープンソース。実務者のために構築されています。

---

## ソースリスト

| リスト | エントリ | バージョン | マッピング済みフレームワーク |
|---|---|---|---|
| [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) | LLM01–LLM10 | 2025 | 20 |
| [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | ASI01–ASI10 | 2026 | 20 |
| [OWASP GenAI Data Security Risks](https://genai.owasp.org/resource/owasp-genai-data-security-risks-mitigations-2026/) | DSGAI01–DSGAI21 | 2026 | 18 |

---

## フレームワークカバレッジマトリックス

| フレームワーク | LLM Top 10 | Agentic Top 10 | DSGAI 2026 |
|---|:---:|:---:|:---:|
| [MITRE ATLAS](https://atlas.mitre.org) | ✅ | ✅ | ✅ |
| [NIST AI RMF 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) | ✅ | ✅ | ✅ |
| [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | ✅ | ✅ | ✅ |
| [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html) | ✅ | ✅ | ✅ |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | ✅ | ✅ | ✅ |
| [ISA/IEC 62443 — OT/ICS](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | ✅ | ✅ | ✅ |
| [MAESTRO — CSA](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | ✅ | ✅ | ✅ |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | ✅ | ✅ | ✅ |
| [CIS Controls v8.1](https://www.cisecurity.org/controls) | ✅ | ✅ | ✅ |
| [OWASP ASVS 4.0.3](https://owasp.org/www-project-application-security-verification-standard/) | ✅ | ✅ | ✅ |
| [SOC 2 Trust Services Criteria](https://www.aicpa-cima.com/resources/landing/2017-trust-services-criteria) | ✅ | ✅ | ✅ |
| [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/) | ✅ | ✅ | ✅ |
| [ENISA Multilayer Framework](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) | ✅ | ✅ | ✅ |
| [OWASP SAMM v2.0](https://owaspsamm.org/) | ✅ | ✅ | ✅ |
| [NIST SP 800-82 Rev 3 — OT/ICS](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) | ✅ | ✅ | ✅ |
| [AIUC-1](https://www.aiuc-1.com) | ✅ | ✅ | ✅ |
| [OWASP NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/) | ✅ | ✅ | ✅ |

---

## 全マッピングファイル

### LLM Top 10 2025 — 20フレームワークマッピング

| ファイル | フレームワーク | 注目コンテンツ |
|---|---|---|
| [LLM_MITREATLAS.md](llm-top10/LLM_MITREATLAS.md) | MITRE ATLAS | 実世界のインシデント参照を含む敵対的技術マッピング |
| [LLM_NISTAIRMF.md](llm-top10/LLM_NISTAIRMF.md) | NIST AI RMF 1.0 | 脆弱性ごとのGOVERN/MAP/MEASURE/MANAGEとAI RMFプロファイル |
| [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) | EU AI Act | 条文レベルの義務、罰金リスク、2026年8月コンプライアンスチェックリスト |
| [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) | ISO/IEC 27001:2022 | ISMS拡張チェックリスト、LLMリスクにマッピングされた2022年新規コントロール |
| [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) | ISO/IEC 42001:2023 | AIMS実装チェックリスト、ISO 27001統合ガイダンス |
| [LLM_CISControls.md](llm-top10/LLM_CISControls.md) | CIS Controls v8.1 | 脆弱性ごとのIG1/IG2/IG3段階別セーフガード |
| [LLM_ASVS.md](llm-top10/LLM_ASVS.md) | OWASP ASVS 4.0.3 | ASVSチェックリスト付きL1/L2/L3検証要件 |
| [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) | ISA/IEC 62443 — OT/ICS | ゾーンモデル、SLレーティング、FR/SR参照、OTデプロイメントチェックリスト |
| [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md) | NIST SP 800-82 Rev 3 | SP 800-53コントロール、米国規制クロスウォーク（NERC CIP、AWIA、CMMC） |
| [LLM_NISTCSF2.md](llm-top10/LLM_NISTCSF2.md) | NIST CSF 2.0 | 新しいGOVERN機能を含む6機能マッピング、CSF 2.0プロファイル |
| [LLM_SOC2.md](llm-top10/LLM_SOC2.md) | SOC 2 Trust Services Criteria | SaaSおよびクラウドLLMデプロイメント向けTSCマッピング |
| [LLM_PCIDSS.md](llm-top10/LLM_PCIDSS.md) | PCI DSS v4.0 | CHDスコープガイダンス、脆弱性ごとのReq 3/6/7/10/11/12 |
| [LLM_ENISA.md](llm-top10/LLM_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3レイヤーマッピング、EU AI ActおよびNIS2整合テーブル |
| [LLM_SAMM.md](llm-top10/LLM_SAMM.md) | OWASP SAMM v2.0 | 脆弱性ごとのL1–L3成熟度ロードマップと記入可能なスコアカード |
| [LLM_STRIDE.md](llm-top10/LLM_STRIDE.md) | STRIDE | LLMエントリごとの6カテゴリ脅威モデルとDFD統合ガイダンス |
| [LLM_CWE_CVE.md](llm-top10/LLM_CWE_CVE.md) | CWE / CVE | CWE根本原因分類とエントリごとの確認済みCVEエビデンステーブル |
| [LLM_AITG.md](llm-top10/LLM_AITG.md) | OWASP AI Testing Guide | 合格基準とCI/CD統合ガイダンス付きLLMエントリごとの構造化テストケース |
| [LLM_MAESTRO.md](llm-top10/LLM_MAESTRO.md) | MAESTRO | 7層アーキテクチャ脅威モデル、レイヤー対LLMマッピング、90分脅威モデリングセッションガイド |
| [LLM_AIUC1.md](llm-top10/LLM_AIUC1.md) | AIUC-1 | LLMデプロイメント向け6ドメインコントロールマッピング — 認証準備チェックリスト |
| [LLM_NHI.md](llm-top10/LLM_NHI.md) | OWASP NHI Top 10 | LLMエントリごとの資格情報およびアイデンティティコントロール — NHIプログラム成熟度テーブル |

### Agentic Top 10 2026 — 20フレームワークマッピング

| ファイル | フレームワーク | 注目コンテンツ |
|---|---|---|
| [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) | AIUC-1 | エージェントAIガバナンス認証コントロールマッピング |
| [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) | MITRE ATLAS | エージェント技術チェーニング、エントリごとのOT増幅要因 |
| [Agentic_NISTAIRMF.md](agentic-top10/Agentic_NISTAIRMF.md) | NIST AI RMF 1.0 | GV-1.7における自律性ポリシーアンカリング、エージェントAI RMFプロファイル |
| [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) | EU AI Act | エントリごとのArt. 14人間による監視、自律性プレミアム罰金分析 |
| [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) | ISO/IEC 27001:2022 | エージェントデプロイメント向けISMS拡張チェックリスト、A.8.2としてのNHI |
| [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) | ISO/IEC 42001:2023 | エントリごとのA.5.2影響評価、EU AI Act整合テーブル |
| [Agentic_NISTCSF2.md](agentic-top10/Agentic_NISTCSF2.md) | NIST CSF 2.0 | GOVERN優先の自律性ポリシーマッピング、エージェントCSF 2.0プロファイル |
| [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) | ISA/IEC 62443 — OT/ICS | エージェントOTゾーンモデル、キルスイッチ設計、SLアップリフトテーブル |
| [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) | MAESTRO — CSA | 7層アーキテクチャ脅威モデル、レイヤー対ASIマッピング、セッションガイド |
| [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) | OWASP NHI Top 10 | 完全なNHI対ASIクロスマッピング、NHIプログラム成熟度テーブル |
| [Agentic_CISControls.md](agentic-top10/Agentic_CISControls.md) | CIS Controls v8.1 | IG1/IG2/IG3セーフガード、CIS 5特権アクセスとして扱われるエージェントNHI |
| [Agentic_ASVS.md](agentic-top10/Agentic_ASVS.md) | OWASP ASVS 4.0.3 | エージェントデプロイメント向けL1/L2/L3検証チェックリスト |
| [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) | OWASP AI Testing Guide | ASI01–ASI10にわたる50の構造化テストケースとデプロイメント前ゲート |
| [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) | OWASP AIVSS | デュアルシナリオスコアリング（監視下 vs 自律）、自律性プレミアム +1.79 |
| [Agentic_ENISA.md](agentic-top10/Agentic_ENISA.md) | ENISA Multilayer Framework | L1/L2/L3レイヤーマッピング、EU AI Act Art. 14/15/52整合、NIS2 Article 23インシデント評価ガイダンス |
| [Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) | SOC 2 Trust Services Criteria | エージェントAI向けTSCマッピング — 自律アクションスコープ、処理整合性、サプライチェーン基準 |
| [Agentic_PCIDSS.md](agentic-top10/Agentic_PCIDSS.md) | PCI DSS v4.0 | 決済システムへのツールアクセスを持つエージェント向けPCI監査ガイダンス、エントリごとのReq 6/7/8/10/11/12 |
| [Agentic_SAMM.md](agentic-top10/Agentic_SAMM.md) | OWASP SAMM v2.0 | エージェントAI向けL1–L3成熟度スコアカード — デプロイメント前ゲートとプログラム成熟度ロードマップ |
| [Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OTエージェント配置、SP 800-53コントロール、米国規制クロスウォーク（NERC CIP、AWIA、CMMC） |

> **このフォルダにも含まれています：** [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — CWE根本原因分類、確認済みCVE、完全なCWEクロスリファレンスインデックス。

### DSGAI 2026 — 18フレームワークマッピング

| ファイル | フレームワーク | 注目コンテンツ |
|---|---|---|
| [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md) | ISO/IEC 27001:2022 | 全21 DSGAIエントリをカバーするISMS拡張 |
| [DSGAI_NISTAIRMF.md](dsgai-2026/DSGAI_NISTAIRMF.md) | NIST AI RMF 1.0 | DSGAIエントリごとのGOVERN/MAP/MEASURE/MANAGEとデータセキュリティプロファイル |
| [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) | EU AI Act | エントリごとの条文レベルの義務、GPAIと高リスクAIのスコープ |
| [DSGAI_NISTCSF2.md](dsgai-2026/DSGAI_NISTCSF2.md) | NIST CSF 2.0 | 全21エントリの6機能マッピング、GenAIデータセキュリティプロファイル |
| [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) | MITRE ATLAS | 敵対的技術マッピング、4つの完全な攻撃パスチェーン |
| [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) | ISA/IEC 62443 — OT/ICS | エントリごとのOT脅威シナリオ、SLレーティング、完全なOTチェックリスト |
| [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) | MAESTRO — CSA | 全21エントリのレイヤー起点分析、DSGAI脅威サーフェスの52%としてのL2データオペレーション |
| [DSGAI_SOC2.md](dsgai-2026/DSGAI_SOC2.md) | SOC 2 Trust Services Criteria | SaaSおよびクラウドGenAIデプロイメント向けTSCマッピング |
| [DSGAI_PCIDSS.md](dsgai-2026/DSGAI_PCIDSS.md) | PCI DSS v4.0 | CHDスコープガイダンス、GenAIデータ向けPCI監査チェックリスト |
| [DSGAI_ASVS.md](dsgai-2026/DSGAI_ASVS.md) | OWASP ASVS 4.0.3 | 全21 DSGAIエントリのL1/L2/L3検証要件、4フェーズ実装優先度 |
| [DSGAI_CISControls.md](dsgai-2026/DSGAI_CISControls.md) | CIS Controls v8.1 | 全21エントリのIG1/IG2/IG3セーフガード、GenAIデータセキュリティ実装グループ |
| [DSGAI_CWE_CVE.md](dsgai-2026/DSGAI_CWE_CVE.md) | CWE / CVE | 全21 DSGAIエントリのCWE根本原因分類と確認済みCVEエビデンス |
| [DSGAI_ENISA.md](dsgai-2026/DSGAI_ENISA.md) | ENISA Multilayer Framework | 全21 DSGAIエントリのL1/L2/L3レイヤーマッピング、EU AI ActおよびNIS2整合 |
| [DSGAI_ISO42001.md](dsgai-2026/DSGAI_ISO42001.md) | ISO/IEC 42001:2023 | DSGAIエントリごとのAIMSコントロール、ISO 27001統合ガイダンス、A.7データガバナンス参照 |
| [DSGAI_SAMM.md](dsgai-2026/DSGAI_SAMM.md) | OWASP SAMM v2.0 | GenAIデータセキュリティ向けL1–L3成熟度スコアカード — GDPRおよび規制コンプライアンスベースライン |
| [DSGAI_NISTSP80082.md](dsgai-2026/DSGAI_NISTSP80082.md) | NIST SP 800-82 Rev 3 | OTデータ配置、DSGAIエントリごとのSP 800-53コントロール、NERC CIP/FISMA/CMMCクロスウォーク |
| [DSGAI_AIUC1.md](dsgai-2026/DSGAI_AIUC1.md) | AIUC-1 | ドメインA（データとプライバシー）がDSGAIエントリの50%以上をカバー — 認証準備テーブル |
| [DSGAI_NHI.md](dsgai-2026/DSGAI_NHI.md) | OWASP NHI Top 10 | DSGAIリスクの有効化条件としてのNHI — GenAIデータ向けNHIプログラム成熟度テーブル |

### 共有リソース

| ファイル | 内容 |
|---|---|
| [shared/RECIPES.md](shared/RECIPES.md) | 動作するPythonによる13のセキュリティ実装パターン — RAG、MCP、OT、エージェント |
| [shared/TOOLS.md](shared/TOOLS.md) | 機能別に整理された40以上のオープンソースセキュリティツール |
| [shared/GLOSSARY.md](shared/GLOSSARY.md) | LLM、ASI、DSGAIソースリスト全体の統一用語集 |
| [shared/SEVERITY.md](shared/SEVERITY.md) | 重大度の定義とAIVSS整合 |
| [shared/TEMPLATE.md](shared/TEMPLATE.md) | 新規マッピングファイル貢献者向けの標準テンプレート |

---

## リポジトリ構造

```text
crosswalk/
│
├── README.md
├── CROSSREF.md                      ← マスタークロスリファレンス：LLM ↔ ASI ↔ DSGAI
├── CONTRIBUTING.md
├── CHANGELOG.md
├── GOVERNANCE.md                    ← メンテナーの役割、PR SLO、意思決定プロセス
├── SECURITY.md
├── CODE_OF_CONDUCT.md
│
├── llm-top10/                       ← LLM01–LLM10 × 20フレームワーク
│   ├── LLM_MITREATLAS.md
│   ├── LLM_NISTAIRMF.md
│   ├── LLM_EUAIAct.md
│   ├── LLM_ISO27001.md
│   ├── LLM_ISO42001.md
│   ├── LLM_CISControls.md
│   ├── LLM_ASVS.md
│   ├── LLM_ISA62443.md              ← OT/ICS
│   ├── LLM_NISTSP80082.md           ← OT/ICS
│   ├── LLM_NISTCSF2.md
│   ├── LLM_SOC2.md
│   ├── LLM_PCIDSS.md
│   ├── LLM_ENISA.md                 ← EU / NIS2
│   ├── LLM_SAMM.md                  ← 成熟度モデル
│   ├── LLM_STRIDE.md                ← 脅威モデリング
│   ├── LLM_CWE_CVE.md               ← 根本原因分類 + CVE
│   ├── LLM_AITG.md                  ← AIテストガイド
│   ├── LLM_MAESTRO.md               ← MAESTRO 7層脅威モデル
│   ├── LLM_AIUC1.md                 ← AIUC-1認証フレームワーク
│   └── LLM_NHI.md                   ← 非人間アイデンティティコントロール
│
├── agentic-top10/                   ← ASI01–ASI10 × 20フレームワーク
│   ├── Agentic_AIUC1.md
│   ├── Agentic_MITREATLAS.md
│   ├── Agentic_NISTAIRMF.md
│   ├── Agentic_EUAIAct.md
│   ├── Agentic_ISO27001.md
│   ├── Agentic_ISO42001.md
│   ├── Agentic_NISTCSF2.md
│   ├── Agentic_ISA62443.md          ← OT/ICS
│   ├── Agentic_MAESTRO.md           ← 脅威モデリング — 7層アーキテクチャ
│   ├── Agentic_OWASP_NHI.md         ← 非人間アイデンティティ
│   ├── Agentic_CISControls.md
│   ├── Agentic_ASVS.md
│   ├── Agentic_AITG.md              ← AIテストガイド — 50テストケース
│   ├── Agentic_AIVSS.md             ← リスクスコアリング — 自律性プレミアム
│   ├── Agentic_CWE_CVE.md           ← CWE分類 + 確認済みCVE
│   ├── Agentic_ENISA.md             ← EU / NIS2
│   ├── Agentic_SOC2.md              ← SOC 2 TSC — エージェントAI監査
│   ├── Agentic_PCIDSS.md            ← PCI DSS v4.0 — 決済システムエージェント
│   ├── Agentic_SAMM.md              ← 成熟度モデル — デプロイメント前ゲート
│   └── Agentic_NISTSP80082.md       ← OT/ICS — 米国規制整合
│
├── dsgai-2026/                      ← DSGAI01–DSGAI21 × 18フレームワーク
│   ├── DSGAI_ISO27001.md
│   ├── DSGAI_NISTAIRMF.md
│   ├── DSGAI_EUAIAct.md
│   ├── DSGAI_NISTCSF2.md
│   ├── DSGAI_MITREATLAS.md
│   ├── DSGAI_ISA62443.md            ← OT/ICS
│   ├── DSGAI_MAESTRO.md             ← 脅威モデリング — データオペレーション視点
│   ├── DSGAI_SOC2.md
│   ├── DSGAI_PCIDSS.md
│   ├── DSGAI_ASVS.md                ← OWASP ASVS 4.0.3
│   ├── DSGAI_CISControls.md         ← CIS Controls v8.1
│   ├── DSGAI_CWE_CVE.md             ← 根本原因分類 + CVE
│   ├── DSGAI_ENISA.md               ← EU / NIS2
│   ├── DSGAI_ISO42001.md            ← AI管理システム
│   ├── DSGAI_SAMM.md                ← 成熟度モデル — データセキュリティプログラム
│   ├── DSGAI_NISTSP80082.md         ← OT/ICS — 米国規制整合
│   ├── DSGAI_AIUC1.md               ← AIUC-1認証フレームワーク
│   └── DSGAI_NHI.md                 ← 非人間アイデンティティ — データパイプライン資格情報
│
├── shared/
│   ├── RECIPES.md                   ← 13の実装パターン（Pythonコード）
│   ├── TOOLS.md                     ← 40以上のオープンソースツールカタログ
│   ├── GLOSSARY.md                  ← 統一用語集
│   ├── SEVERITY.md                  ← 重大度の定義 + AIVSS整合
│   └── TEMPLATE.md                  ← 新規マッピングファイル向け標準テンプレート
│
├── data/
│   ├── schema.json                  ← JSON Schema（Draft 7）エントリファイル用
│   ├── incidents.json               ← MAESTROレイヤー帰属付き20インシデント
│   ├── incidents-schema.json        ← インシデント用JSON Schema
│   ├── entries/                     ← 41の機械可読エントリJSONファイル
│   └── README.md                    ← データレイヤードキュメント、jqクエリ例
│
├── scripts/
│   ├── validate.js                  ← コンテンツバリデーター（セクション、リンク、カウント）
│   ├── generate.js                  ← Markdown-to-JSONパーサー → data/entries/
│   └── compliance-report.js         ← ギャップ評価ジェネレーター（MD / CSV / JSON）
│
├── evals/
│   ├── README.md                    ← セットアップガイドと結果の解釈
│   ├── garak/                       ← 7 YAMLプロファイル（LLM01/02/04/07/09、ASI01/05）
│   ├── pyrit/                       ← 3つの非同期Pythonスクリプト（LLM01、DSGAI04、ASI01）
│   ├── laaf/                        ← LAAF v2.0 LPCIスイート（S1–S6 + クロスウォークレポーター）
│   └── ci/                          ← github-action.yml — ドロップインCI/CDテンプレート
│
└── i18n/
    ├── WORKFLOW.md                  ← 翻訳貢献者ガイド
    ├── es/                          ← スペイン語（PR受付中）
    ├── fr/                          ← フランス語（PR受付中）
    └── pt/                          ← ポルトガル語（PR受付中）
```

---

## コンプライアンスギャップレポート

データレイヤーからフレームワーク固有のギャップ評価を数秒で生成できます：

```bash
node scripts/compliance-report.js                          # 全17フレームワーク → reports/
node scripts/compliance-report.js --framework "EU AI Act"  # 1つのフレームワーク
node scripts/compliance-report.js --format csv             # Excel互換
node scripts/compliance-report.js --format json            # 機械可読
node scripts/compliance-report.js --list-frameworks        # 全オプションを表示
```

各レポートには、エグゼクティブサマリー、カバレッジマトリックス（OWASPエントリ × コントロール）、ノート付きコントロール別詳細、および優先度付きアクションプランが含まれます。

## LAAF v2.0 — LPCIレッドチーミング

[LAAF v2.0](https://github.com/qorvexconsulting1/laaf-V2.0)は、GarakおよびPyRITと並ぶ3番目の評価フレームワークとして統合されています。表面レベルのインジェクションテストでは見逃される攻撃サーフェスをカバーします：メモリ永続化、レイヤードエンコーディング、セマンティックリフレーミング、および6ステージライフサイクル攻撃。

```bash
pip install git+https://github.com/qorvexconsulting1/laaf-V2.0.git
export OPENAI_API_KEY=sk-...
bash evals/laaf/run_laaf.sh           # S1–S6フルスイート
laaf scan --target mock --dry-run     # APIキー不要
```

| LAAFステージ | OWASP | しきい値 |
|---|---|---|
| S1 偵察 | LLM07, LLM01 | 0% |
| S2 ロジックレイヤーインジェクション | LLM01, ASI01, DSGAI04 | 5% |
| S3 トリガー実行 | ASI01, ASI06, LLM06 | 0% |
| S4 永続化 | ASI06, LLM06, DSGAI04 | 0% |
| S5 回避 | LLM01, LLM02 | 10% |
| S6 トレース改ざん | DSGAI01, LLM07 | 0% |

完全なLPCI攻撃ベクトル → OWASP → MAESTROクロスウォークについては`evals/laaf/README.md`をご覧ください。

---

## インシデントトラッカー

OWASPエントリおよびMAESTROアーキテクチャレイヤーにマッピングされた、20の実世界および研究実証済みインシデント：

```bash
node scripts/incidents-report.js                      # 全インシデント → reports/incidents.md
node scripts/incidents-report.js --entry LLM01        # 特定エントリのインシデント
node scripts/incidents-report.js --layer L3           # Agent Frameworksに関連するインシデント
node scripts/incidents-report.js --category real-world
node scripts/incidents-report.js --format csv         # Excelエクスポート
```

インシデントごとに追跡されるMAESTROレイヤーの役割：**オリジン**（攻撃の開始地点） · **伝播**（拡散の方法） · **インパクト**（被害が発現する場所） · **ブラインドスポット**（検知が失敗した場所）。

---

## ここから始めましょう — 役割別

60秒以内にエントリポイントを見つけてください。

**2026年8月までにEU AI Actに準拠する必要がある場合**
→ 開始：[LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) — 条文レベルの義務、罰金リスク、コンプライアンスチェックリスト
→ 次に：[Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) 自律エージェントをデプロイしている場合（Art. 14人間による監視）
→ 次に：[DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md) GPAIモデルのスコープとデータガバナンス義務について

**自律AIエージェントをデプロイしており、何が問題になり得るか知りたい場合**
→ 開始：[CROSSREF.md](CROSSREF.md) — 全41脆弱性IDのマスタークロスリファレンス
→ 次に：[Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — アーキテクチャ脅威モデル（各リスクはどこで発生するか？）
→ 次に：[Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — 各リスクをスコアリング；自律性により平均+1.79の重大度上昇
→ 次に：[Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — アイデンティティおよび資格情報コントロール

**SOC 2監査人またはGRC専門家がGenAIコントロール評価を準備している場合**
→ 開始：[LLM_SOC2.md](llm-top10/LLM_SOC2.md) — SaaS/クラウドLLMデプロイメント向けTSCマッピング
→ 次に：[Agentic_SOC2.md](agentic-top10/Agentic_SOC2.md) — 自律アクションスコープ、処理整合性基準
→ 次に：[LLM_SAMM.md](llm-top10/LLM_SAMM.md) — プログラムの完全性を証明するための記入可能なSAMM成熟度スコアカード

**AppSecエンジニアまたはレッドチーマーがテスト計画を作成している場合**
→ 開始：[Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 合格基準とCI/CDゲート付き50の構造化テストケース
→ 次に：[DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — 4つの完全な攻撃チェーンを含む攻撃者TTPマッピング
→ 次に：[shared/RECIPES.md](shared/RECIPES.md) — テスト対象のコントロールを実装するための13の動作するPythonパターン

**OT/ICS環境（エネルギー、ユーティリティ、製造業）にデプロイされたAIをセキュリティ保護している場合**
→ 開始：[Agentic_NISTSP80082.md](agentic-top10/Agentic_NISTSP80082.md) — OTゾーンモデル、SP 800-53コントロール、NERC CIP/AWIA/CMMCクロスウォーク
→ 次に：[Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) — SLレーティング、ゾーンモデル、キルスイッチ設計
→ 次に：[DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) — OTにおけるRAGコーパスポイズニング（安全手順操作シナリオ）

---

## クイックナビゲーション

**2026年8月までのEU AI Actコンプライアンス**
→ [LLM_EUAIAct.md](llm-top10/LLM_EUAIAct.md) · [Agentic_EUAIAct.md](agentic-top10/Agentic_EUAIAct.md) · [DSGAI_EUAIAct.md](dsgai-2026/DSGAI_EUAIAct.md)

**NIS2の対象となる欧州の組織**
→ [LLM_ENISA.md](llm-top10/LLM_ENISA.md) — NIS2 Article 23インシデント評価ガイダンス付きENISAフレームワーク

**OT/ICS環境におけるAI**
→ [LLM_ISA62443.md](llm-top10/LLM_ISA62443.md) · [Agentic_ISA62443.md](agentic-top10/Agentic_ISA62443.md) · [DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md) · [LLM_NISTSP80082.md](llm-top10/LLM_NISTSP80082.md)

**自律エージェントのデプロイ**
→ [Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md) — アイデンティティガバナンス
→ [Agentic_AIUC1.md](agentic-top10/Agentic_AIUC1.md) — エージェントガバナンス認証
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — 自律性プレミアム付きリスクスコアリング

**コントロール選択前のエージェントAIシステムの脅威モデリング**
→ [Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md) — セッションガイド付きMAESTRO 7層脅威列挙
→ [DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md) — 全21 DSGAIエントリのMAESTROデータオペレーション視点

**GenAI向けISO 27001 ISMS拡張**
→ [LLM_ISO27001.md](llm-top10/LLM_ISO27001.md) · [Agentic_ISO27001.md](agentic-top10/Agentic_ISO27001.md) · [DSGAI_ISO27001.md](dsgai-2026/DSGAI_ISO27001.md)

**AIガバナンス向けISO 42001 AIMS**
→ [LLM_ISO42001.md](llm-top10/LLM_ISO42001.md) · [Agentic_ISO42001.md](agentic-top10/Agentic_ISO42001.md) — EU AI Actコンプライアンスエビデンステーブル付き

**セキュリティプログラム成熟度**
→ [LLM_SAMM.md](llm-top10/LLM_SAMM.md) — 記入可能なスコアカード付きSAMM L1–L3ロードマップ

**エージェントAI向けセキュリティテスト計画**
→ [Agentic_AITG.md](agentic-top10/Agentic_AITG.md) — 50の構造化テストケース、デプロイメント前ゲート、OTアデンダム

**エージェントAI向けリスクレジスタースコアリング**
→ [Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md) — 監視下 vs 自律のデュアルシナリオスコアリング、平均自律性プレミアム +1.79

**GenAIリスクに対する攻撃者の視点**
→ [DSGAI_MITREATLAS.md](dsgai-2026/DSGAI_MITREATLAS.md) — ATLAS技術マッピング、4つの攻撃パスチェーン
→ [Agentic_MITREATLAS.md](agentic-top10/Agentic_MITREATLAS.md) — エージェント技術チェーニング

**CWE根本原因と確認済みCVE**
→ [Agentic_CWE_CVE.md](agentic-top10/Agentic_CWE_CVE.md) — 根本原因分類、CVEエビデンス、クロスリファレンスインデックス

**フレームワーク理論ではなく実装コード**
→ [shared/RECIPES.md](shared/RECIPES.md) — 動作するPythonによる13の本番パターン

**3つのソースリスト全体のすべてのリスク**
→ [CROSSREF.md](CROSSREF.md) — マスタークロスリファレンス

---

## 注目のカバレッジ

### 完全なOT/ICSトリロジー

3つのOWASP GenAIソースリストすべてをISA/IEC 62443およびNIST SP 800-82 Rev 3にマッピングした、唯一の公開リソースです。ゾーンモデル配置、セキュリティレベルレーティング、基本要件およびセキュリティ要件の参照、OT固有の脅威シナリオ、および各ソースリストのデプロイメント前チェックリストが含まれています。

[DSGAI_ISA62443.md](dsgai-2026/DSGAI_ISA62443.md)のRAGコーパスポイズニングシナリオ — OTネットワークへのアクセスなしにメンテナンス間隔を変更する安全手順操作攻撃 — は、公開ドキュメントの他のどこにも存在しません。

### MAESTRO 7層脅威モデリング

[Agentic_MAESTRO.md](agentic-top10/Agentic_MAESTRO.md)と[DSGAI_MAESTRO.md](dsgai-2026/DSGAI_MAESTRO.md)は、OWASP GenAIリスクをCloud Security AllianceのMAESTROフレームワークにマッピングした唯一の公開ドキュメントです。このリポジトリの他のすべてのファイル — リスクをコントロールにマッピングするもの — とは異なり、MAESTROは各リスクを**それが発生するアーキテクチャレイヤー**にマッピングし、どのチームが問題を所有し、システムのどこに修正をデプロイすべきかを示します。

DSGAIマッピングからの主要な発見：**L2データオペレーションは全DSGAIエントリの52%の発生元レイヤーです**。RAGコーパス、エンベディングストア、トレーニングパイプライン、メモリシステムをセキュリティクリティカルなインフラストラクチャとして扱わない組織は、GenAIデータセキュリティ脅威ランドスケープの大部分に対して防御が不十分です。

### エージェント自律性プレミアム

[Agentic_AIVSS.md](agentic-top10/Agentic_AIVSS.md)は、人間による監視を除去することのリスクコストを定量化しています：全10のエージェントエントリで平均**+1.79 AIVSS重大度ポイント**。人間による監視の除去は10エントリ中7つを「高」から「クリティカル」に変換します — EU AI Act Article 14に基づく義務的人間監視の定量的根拠です。

### 完全なエージェントアイデンティティカバレッジ

[Agentic_OWASP_NHI.md](agentic-top10/Agentic_OWASP_NHI.md)は、すべてのNHI Top 10エントリをすべてのASIエントリにマッピングしています — エージェントセキュリティリスクをIAMチームが既に運用しているNHIコントロールに変換した唯一の公開ドキュメントです。

### SAMM成熟度スコアカード

[LLM_SAMM.md](llm-top10/LLM_SAMM.md)には、すべてのLLM本番デプロイメントに対するSAMMプラクティスごとの最小限の実行可能レベルを持つ記入可能な成熟度スコアカードが含まれています — セキュリティプログラムリーダーがエンジニアリングリーダーシップに対してプログラムの現在地と次に改善すべき事項を報告するために使用する成果物です。

### 本番環境実装レシピ

[shared/RECIPES.md](shared/RECIPES.md)には、動作するPythonによる13の本番環境対応セキュリティパターンが含まれています：アクセス制御付きRAG取得、MCPディスクリプター整合性検証、JIT資格情報発行、OTキルスイッチ、行動ベースライン監視、カスケード封じ込め、人間確認ゲート。

---

## コントリビューション

コントリビューションを歓迎します — 新しいフレームワークマッピング、更新されたコントロール、新しい実装レシピ、翻訳、追加ツールエントリ。

ファイルテンプレート、PRプロセス、およびコントリビューションガイドラインについては[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。すべてのコントリビューターはCHANGELOGに記載されています。

---

## ライセンス

[Creative Commons Attribution-ShareAlike 4.0 International](LICENSE)

適切なクレジットと同じライセンスの下での配布により、商用利用を含むあらゆる目的で自由に共有および改変できます。

---

## 謝辞

**[Emmanuel Guilherme Junior](https://github.com/emmanuelgjr)**と[OWASP GenAI Data Security Initiative](https://genai.owasp.org)により作成・維持管理されています。

OWASP LLM Top 10、OWASP Agentic Top 10、OWASP GenAI Data Security、OWASP NHI Top 10、およびOWASP SAMMプロジェクトチームの成果の上に構築されています。

MAESTROフレームワークとOWASP LLM Top 10への貢献について、[Ken Huang](https://github.com/kenhuangus)氏（Cloud Security Alliance）に特別な感謝を申し上げます。

---

*[genai.owasp.org](https://genai.owasp.org) · [CC BY-SA 4.0](LICENSE)*
