# Agent workflow 說明

## 第一步
- 請先閱讀 `index.html`的內容 。
    - windows  mac os 就直接點擊該檔案 , linux ```bash firefox index.html ```
    - 點教學卡可查看講解、提示詞、停止條件、
    - 練習答案與講者節奏,這邊可以請您指派 Agent 擔任您的導師。
    - 無須 web server；課程與圖可離線使用。 

## 第二步 檔案內容說明

| 位置 | 用途 |
|---|---|
| `index.html` | 互動式架構說明網站 |
| `skills/` | 12 個 skills：`workflow` 統一入口，以及 11 個通用 skills 與附屬參考文件 |
| `skills/workflow/SKILL.md` | 英文流程入口：續接摘要、以 change 為停點、跨專案累計與結案詢問 |
| `skills/workflow/references/customization.md` | 自訂位置對照、使用範例與行為驗收情境 |
| `course/workflow.html` | Archify 產生的互動架構圖 |
| `course/workflow.json` | 可再次編輯、驗證的 Archify 內容的檔案 |
| `course/lesson.json` | 8 張教學卡的資料，包含講解、提示詞、停止條件、練習答案、講者節奏與來源引用；合計 90 分鐘 |
| `course/speaker-notes.zh-TW.md` | 90 分鐘、8 段課程的講者教案，對應 `course/lesson.json` 的 8 張教學卡；可請 Agent 依此擔任導師 |
| `course/weekly-runbook.zh-TW.md` | Wiki 與 Skill 在每次任務、每週、每月的維護流程，供維護者使用；不是網頁執行內容，也不會自行啟動排程 |
| `course/source-index.zh-TW.md` | 說明來源矩陣、論文、工具、Wiki 快照與驗證限制，協助理解 `course/sources/` 的來源與可信範圍 |
| `course/sources/workflow.md` | 主工作流與 OpenSpec 文件責任；被第 1、2、3、4、6 張課程卡引用 |
| `course/sources/project-toolbox.md` | MCP、CLI、查詢與測試工具的路由及用途；被第 1、5 張課程卡引用 |
| `course/sources/wiki-context.md` | Context packet（上下文資料包）、問題範圍與 claim boundary（結論可支持的範圍）；被第 3、7 張課程卡引用 |
| `course/sources/wiki-governance.md` | Wiki metadata（中繼資料）、證據層級、人審與 capture（知識留存）流程；被第 6、7、8 張課程卡引用 |
| `course/sources/wiki-index.md` | Wiki 導航與知識分類入口；被第 7 張課程卡引用 |
| `course/sources/wiki-skill.md` | Wiki Skill 的 query（查詢）、ingest（來源匯入）、演進與候選規則；被第 7、8 張課程卡引用 |
| `course/ARCHIFY-THIRD-PARTY-NOTICES.md` | `course/workflow.html` 使用的第三方資產授權聲明，屬於授權文件 |
| `install.py` | 將 skills 安裝到指定練習 repo 的 `.agents/skills`；衝突時拒絕覆蓋 |
| `verify.py` | 檢查教材資料、檔案完整性與安裝拒絕路徑 |

課程卡編號依 `course/lesson.json` 的排列順序。`course/sources/` 是唯讀教學快照，內部連結與原始碼定位仍以原專案為準，並非獨立可執行的 Wiki；工具健康快照也不代表當下可用狀態，詳細限制請參閱 `course/source-index.zh-TW.md`。

## 第三步 安裝該專案的skill

```bash
python3 verify.py
python3 install.py /absolute/path/to/your-practice-repo
```

- 安裝完成後，在目標練習專案啟用：

```text
$workflow
請啟動或接續目前專案，先簡要說明實作目標、進度、下一步與 OpenSpec 路徑。
```

若目前環境尚未辨識新安裝的 skill，可明確請 Agent 讀取
`.agents/skills/workflow/SKILL.md` 並依其指引執行。

初始模式會在每個完整 change 結束後停下；change 內接續規格、實作、
驗證與同步封存。整個大專案納入的 changes 全部完成才累計一次 workflow。
同一台電腦的同一使用者跨專案累計滿 5 次後，詢問是否改為自動接續 changes；
拒絕後不再主動重問，隨時可要求切換或切回。每個完整 workflow 結案後，
另行詢問是否進行 Skill／Wiki 整理。

共用紀錄預設存在使用者家目錄的 `.workflow/state.json`，不放進教材或練習 repo。
安裝不建立該紀錄；實際啟用後需要保存時，若環境限制家目錄寫入，Agent 會走
環境授權流程。OpenSpec CLI 與目標專案設定須可用；Wiki 則依目標專案另行提供。
Skill 指引使用英文，Agent 仍依使用者語言回報。

維護者驗證：`python3 -B -m unittest discover -s tests`；紀錄工具測試使用暫存目錄。
Windows 若無 `python3` 指令，可使用 `python`。

## 備註

- 目標專案的路徑必須存在

- 若目標專案中有同名 skill 則安裝會先停止,以確保不覆蓋既原始專案內的skill

- 本安裝包 __不__ 修改目標專案的 AGENTS.md、OpenSpec 設定或 MCP 設定, 請您發揮想像力與您的Agent 討論

- MCP 請參閱附錄的 `tool_refer.txt` 內的網址,並自行安裝
