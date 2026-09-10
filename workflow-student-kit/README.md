# Agent workflow 教材

每個 change 結束時，archive 技能會在該 change 內建立 `code-trace.md`，
隨歸檔保存並在完成報告提供位置。內容包含主程式、測試、需求與專案管理文件的
實際目錄樹、絕對／專案相對路徑、用途，以及需求 → 程式入口 → 測試與執行證據的對照。
樹狀圖依專案真實檔名與層級產生，不套用固定分類；大型專案可展開相關分支並標明省略範圍。
既有 OpenSpec 需求直接連結，不另複製 `requirements.md`；測試數量依實際驗收要求，
不把未執行的測試標為通過。
格式與檢查由 [code trace 指引](skills/openspec-archive-change/references/code-trace.md) 統一維護。

直接開啟 `index.html`，可離線閱讀互動流程圖及 8 段、90 分鐘教學。
Skill 與管理範本使用英文，Agent 仍依使用者語言說明。

## 檔案配置

| 位置 | 用途 |
|---|---|
| `index.html` | 三段系統流程與互動課程卡 |
| `course/workflow.archify.json`、`workflow.html` | Archify Workflow v2 原始規格與離線互動圖 |
| `course/lesson.json` | 8 張課程卡、練習與目前實作引用 |
| `course/build.py` | 從資料重建流程圖與首頁課程資料 |
| `course/speaker-notes.zh-TW.md` | 與課程卡對應的講者教案 |
| `course/weekly-runbook.zh-TW.md` | 維護節奏與品質演進 |
| `course/sources/` | 原 RedCap 歷史唯讀快照，不是現行操作規則 |
| `docs/tools.md` | 工具能力、情境、限制、檢查與安裝來源 |
| `docs/skill-contracts.md` | 14 個技能的責任、架構銜接與驗收對照 |
| `management/AGENTS.md` | 學員專案規則範本 |
| `management/openspec-project/` | 各專案工具路由 spec 與 Toolbox 範本 |
| `skills/` | 14 個技能，含 workflow、llm-wiki、skill-evolution |
| `install.py` | 安裝技能及 docs／management 資源，衝突時拒絕 |
| `verify.py`、`tests/` | 教材一致性、安裝、狀態及候選檢查 |

根目錄 AGENTS.md 管理本教材。原 spec.md 與 redcap_toolbox.md
已通用化到 management/openspec-project/；本教材不建立實際 openspec/ 或 wiki/。

## 安裝到練習專案

```bash
python3 -B verify.py
python3 install.py /absolute/path/to/your-practice-repo
```

Windows 若無 python3，使用 python。目標目錄須已存在。安裝產物：

```text
<target>/.agents/skills/<14 skills>/
<target>/.agents/workflow-kit/docs/
<target>/.agents/workflow-kit/management/
```

不覆蓋同名 skills 或既有 workflow-kit 資源，不修改目標 AGENTS.md、
OpenSpec／MCP 設定或個人進度。既有安裝先比較差異並選擇更新範圍；
不要以刪除既有技能作為預設升級方式。

## 啟動與專案接入

依工具指南準備適用工具及 OpenSpec CLI。各工具的入口形式不同；
安裝連結不代表已健康或每個任務都需要。

```text
$workflow
請啟動或接續目前專案，先說明目標、進度、下一步與 OpenSpec 路徑。
```

若尚未辨識技能，請 Agent 讀 `.agents/skills/workflow/SKILL.md`。
首次接入時依問題選工具，使用安裝資源中的 management 範本，
把實際專案契約放在對應 OpenSpec，例如：

```text
<project>/openspec/projects/<project-key>/spec.md
<project>/openspec/projects/<project-key>/toolbox.md
```

projects/ 是本教材分組慣例，不是 OpenSpec CLI schema。沿用現有設定，
change／artifact 路徑仍由 CLI 解析；有多個專案時先選擇。
Agent 在既有授權內接入，不直接覆蓋整份 AGENTS.md。

## 推進與品質演進

- 完整 change 結束後停下；其內接續規格、實作、驗證、同步封存。
- 所有 changes 與整體驗收完成才計一次 workflow。
- 同一本機使用者跨專案滿 5 次詢問是否自動接續；拒絕後不再主動重問。
  共用索引位於使用者家目錄的 `.workflow/state.json`，隨時可要求切換模式。
- 完整結案後詢問 Wiki 整理；每次 Wiki 更新後自動評估 Skill 改進。
- 已確認路徑、連結與命令筆誤直接修復驗證；品質候選需重複根因兩次、
  成功／失敗證據及可執行比較。
- 候選隔離在專案 Wiki 的 evolution/。同一版本通過兩個不同任務，
  至少一個未用於撰寫候選；版本改變重驗。正確性／完整性優先。
- 穩定後提出更新建議，由使用者決定指定版本與本機／共用目標。
  拒絕與回退結果保留在 Wiki；回饋不遞迴觸發評估。

安裝不建立個人狀態或 Wiki；實際家目錄寫入依環境權限處理。
llm-wiki 是本套件本地技能，不需要外部 LLM Wiki 桌面程式才能操作。

## 維護與驗證

```bash
python3 -B course/build.py
python3 -B -m unittest discover -s tests
python3 -B verify.py
```

修改後同步 PROVENANCE.json 與 SHA256SUMS。
有 Chromium／Edge 時可執行：

```text
node tests/test_course_browser.mjs <browser-executable> <screenshot-directory>
```

測試使用暫存專案，不寫個人進度或啟用共用 Skill。候選檢查工具只驗證紀錄；
真實 Agent 品質仍須實跑案例並判讀證據。
`course/build.py` 預設只同步課程文字，不覆寫架構圖。修改圖面請編輯
`course/workflow.archify.json`，並使用本機 Archify 專案重新生成：

```text
python -B course/build.py --archify-root ../archify
node ../archify/archify/bin/archify.mjs visual-check course/workflow.html --json
```

找不到 Chrome 時，可將 `ARCHIFY_CHROME` 環境變數設為已安裝的 Edge／Chromium 執行檔。
閱讀教材不需要安裝 Archify；只有重新生成圖面時才需要本機 CLI。
現行圖面使用 Archify 2.17.0-dev.1，繁體中文內容搭配英文固定工具列。
新驗收紀錄為 `course/workflow.delivery.json` 與 `course/workflow.visual-check.json`；
舊 `archify-delivery.json`、`archify-browser.json` 留作歷史紀錄。
桌面四種尺寸已驗證；手機需使用縮放／平移，390px 寬度下固定工具列可能部分超出可視區。
