# 課程來源與驗證範圍

查核日期：2026-09-09。相對路徑從講師的 RedCap experimental 專案根目錄解析。`sources/` 是只讀教學快照，内部連結與原始碼定位仍以原專案為準，並非獨立可執行的 wiki。

## 來源矩陣

| 來源 | 定位 | 支持的教材內容 | 邊界 |
|---|---|---|---|
| 主工作流 | `.agents/skills/grill-with-docs/workflow.md`；快照 `sources/workflow.md` | propose／apply／review 的架構核對、文件責任與停止條件 | 程序規則，非某次 runtime 的成功證據 |
| 專案規則 | `AGENTS.md` 的 File Query Workflow | Symdex MCP／CLI、RTK、直接文件讀取分工 | 實際可呼叫工具與權限仍需當次確認 |
| 工具箱 | `agent_doc/Project_management/redcap_toolbox.md`；快照 `sources/project-toolbox.md` | 工具用途與命令參考 | health 表是 2026-06-27 快照，未全部重測 |
| Wiki 治理 | `redcap_research_wiki/governance.md`；快照 `sources/wiki-governance.md` | metadata、evidence tiers、human promotion、capture triage | 人審與結論正確性不由格式檢查器代替 |
| Wiki 導航 | `redcap_research_wiki/index.md`；快照 `sources/wiki-index.md` | 找 RedCap、A-IoT、xApp／dApp 與決策頁 | 導航不等於讀過全部原始碼 |
| Context packet | `redcap_research_wiki/CONTEXT.md`；快照 `sources/wiki-context.md` | 問題、來源、claim boundary、critical_check | 這份是 wiki packet 契約，不是 generic domain glossary |
| Active wiki skill | `redcap_library/skills/redcap_research_wiki/SKILL.md`；快照 `sources/wiki-skill.md` | Runner、Evolution Worker、Water Spider、WIP = 1、人審 | 本專案採用的受限流程，非論文完整自動實驗 |
| WikiSkill 論文 | `agent_doc/wikiskill.pdf` 第 4 頁圖 2、§3.1；第 5–6 頁 §3.2.1–3.2.4 | 三層、四步、validation gating、skill rollback 與 wiki 留存 | benchmark 不直接推論 RedCap 改善；本次未重跑論文 |
| Registry | `redcap_library/bash_tool/registry.json` 的兩個 wiki 驗證條目 | 操作入口、輸出與副作用 | manifest 需求仍依 root 規則；普通唯讀檢查不額外建長任務 manifest |
| Archify | [官方專案](https://github.com/tt-a1i/archify)；本機套件 2.17.0-dev.1 | workflow JSON → HTML；固定工具列英文 | 本次使用既有暫存套件，未修改或升級安裝 |
| MCP | [官方架構說明](https://modelcontextprotocol.io/docs/learn/architecture) | host／client／server、工具與資源分工 | 無法推論某個 server 今日健康 |
| Skills | [官方技能說明](https://learn.chatgpt.com/docs/build-skills) | Skills 包裝指引與資源 | 各 host 支援的發現方式與工具名稱須依版本核對 |

論文書目：Liyan Tang、Cyrus Rashtchian、Chun-Sung Ferng、Andrew Tomkins、Da-Cheng Juan、Tu Vu，*WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution*，本地 PDF 標記 arXiv:2608.27454v1、2026-08-28。[論文定位](https://arxiv.org/abs/2608.27454)。教材以本地 PDF 實際內容為準；PDF 原檔未打入通用下載包。

## 論文到專案的對照

| 論文機制 | 本專案對應 | 不能混為一談 |
|---|---|---|
| Immutable Raw traces | 保留命令、輸出與原始證據路徑 | 沒有宣稱已部署論文完整 raw workspace |
| Persistent Wiki | sources／concepts／systems／decisions／cases／log | 本專案另有 evidence tier、review-required／confirmed |
| Skill Proposer | Evolution Worker 提出最小候選 | Water Spider 是本專案 pull-only 資格規則，不是論文角色名稱 |
| 分數嚴格提升才保留 | 唯讀驗證後由人審啟用 | 文字契約 PASS 不等於實驗分數改善 |
| 拒絕時回退 skill，wiki 留存 | 維持 active skill，保留拒絕理由與歷史 | 本次沒有部署自動回退 daemon |
| 訓練 rollout 限制 wiki access | 本專案 Runner 按 active skill 的 Load Contracts | 不把論文實驗隔離設定誤寫成 repo 全域規則 |

## Research Reading Card

- 問題：如何在現行開發工作流保留知識並更新 skill，又避免無證據自我修改？
- 範圍：教學流程、規格／工具／知識的關係；不修改 wiki 語意、不執行 RFsim、不啟用排程。
- 已見證據：工作流與治理檔案存在；PDF 方法可定位；兩個既有唯讀驗證命令通過。
- 競爭解釋 A：新候選修復了重複根因。
- 競爭解釋 B：案例、環境或評分條件改變，或只是記住了訓練案例。
- 區分方式：在相同條件比較原版與候選，包含未用於提出候選的正面與反例案例，保留輸入版本和輸出。
- 反證：原版也能通過同一案例、候選破壞反例／拒絕條件，或只有文字匹配 PASS；不足以支持候選改善。
- 結論：三層方法可作整理框架；此 repo 目前採受限、人審的演進契約。週期表是教材建議，不是已運行自動化。
- 下一步：由維護者按週期作業選一個有界操作；候選符合門檻再驗證與人審。

## 本次驗證

```text
REDCAP_RESEARCH_WIKI_CHECK PASS pages=26
RESEARCH_WIKI_SKILL_EVOLUTION_CONTRACT PASS bounded_packet=1 refusal=1 wip=1 human_promotion=1
```

第一項檢查 wiki 結構；第二項原腳本使用字串匹配確認規則存在。本課明確不把第二項當作實際 refusal、promotion 或效能測試。

Archify：`archify-delivery.json` 記錄 JSON／HTML 雜湊與 9/9 檢查；`archify-browser.json` 記錄四種桌面尺寸檢查；`workflow.visual-check.*.png` 保留原圖截圖。原始 receipt 含建置暫存路徑，交付後以 SHA-256 對應相同位元組。

教材：`course-browser.json` 記錄 8 張卡片、答案、下一段、Esc 與桌面／手機寬度檢查。`course-preview.png`／`card-preview.png` 是實際瀏覽器畫面。圖與卡片均經視覺檢視；長內容按正常頁面與對話框捲動，不裁掉教學內容。

下載包：根目錄 `verify.py` 可在離線環境檢查 90 分鐘配置、來源、11 個 skills、安裝與拒絕覆蓋；`SHA256SUMS` 檢查交付位元組。
