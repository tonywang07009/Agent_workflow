# Wiki 與 Skill 定期更新作業

這是課程建議的手動節奏，尚未安裝背景排程。每個操作各自完成、回報，再開始下一個；不把不同 wiki operation 合併成一次 invocation。

| 時機 | 執行者 | 單次動作 | 產物／完成條件 |
|---|---|---|---|
| 每次任務完成 | Runner／任務執行者 | 保留命令、輸入版本、退出碼、輸出與原始證據 | 可追溯結果；不用完整對話或私人憑證充當證據 |
| 任務結果值得留存 | Wiki 維護者 | 單獨 `capture-triage` | none／log／update-page／case-draft／decision-contract |
| 每週固定時段 | 維護者 | 先單獨 `lint` | 結構問題與語意問題分開列；不可自動 confirmed |
| lint 完成後 | 維護者 | 一個有界 `ingest` 或其他明確 operation | 優先更新既有頁，保留 source_refs、review-required 與 log |
| 每月或同根因重複時 | 候選提出者 | 檢查 pull rule，符合才由 Evolution Worker 提一個候選 | WIP = 1；不符合則不建立、不啟用 |
| 候選完成 | 驗證者與人類 reviewer | 先用註冊唯讀工具驗證，再由人決定 | 啟用、拒絕或維持原版；保留拒絕理由與版本差異 |

## 一次每週作業的操作順序

1. 確認專案根目錄與 `redcap_research_wiki/index.md`。
2. 查 `redcap_library/bash_tool/registry.json` 的 `validate_redcap_research_wiki`，確認副作用為唯讀。
3. 執行一次 `lint`，報告格式、路徑、metadata、陳舊／矛盾結論。
4. 結束 lint。只有有可重用新證據時，另開一個有界整理操作；否則記錄無須更新。
5. 結論型 query／decide／case-draft 先依 `CONTEXT.md` 建立 packet：問題、來源、證據要求、claim boundary、停止條件；加上 counter explanation、discriminating evidence、falsifier。
6. 內容先維持 draft／review-required；寫入索引與活動紀錄。人類負責 confirmed，validator 不負責語意批准。
7. Skill 演進是另一條路：同根因至少兩次並有正反證據，最多兩條代表 trace、一個已審 pattern／case、一個現有驗證命令。Water Spider 不修改任何 active state。
8. 候選含 applicability、counterexample、stop_condition、validation_command: registered_read_only_tool、非空 rejection_reason。先驗證再人審；未通過就保留 active skill。

本專案原始 wiki authored prose 依 active skill 採英文；本教材是繁體中文導讀。若課堂只要繁體中文講解，勿順便改寫 wiki 語言政策。

## 可複製提示詞

### 本週只做健康檢查

```text
使用 redcap_library/skills/redcap_research_wiki/SKILL.md。
operation: lint
目標：本週 wiki 健康檢查。只使用 registry 已註冊的唯讀驗證。
分開列出結構問題、來源失效、矛盾與需要人審的結論。
不改技術結論，不升級 confirmed，不產生 skill 候選。
```

### 有新證據後，另做 capture-triage

```text
operation: capture-triage
bounded evidence: <一份已完成任務的來源與 log 路徑>
先判斷 none／log／update-page／case-draft／decision-contract。
若會產生結論型 artifact，先建立 context packet；case-draft 加 critical_check。
不得重寫舊實驗結果，不得宣稱未量測的效果。
```

### 候選資格不足的練習

```text
同根因在兩條失敗 trace 重複，但沒有成功對照。
依 Water Spider pull rule 判斷資格。
只說明拒絕理由與下一個最小取證動作；不要建立或啟用候選。
```

預期：缺正面證據；取得同範圍成功 trace 後再判斷。不得先寫一份「待補證據」的 active skill。

## 驗證強度要分清

- `validate_redcap_research_wiki.py`：結構、metadata、連結與標籤檢查。
- `test_research_wiki_skill_evolution.sh`：以字串存在檢查演進契約文字。
- 上述 PASS 不證明 runner 在真實任務中正確拒絕、候選改善成效或自動回退成功。
- 真正候選評估須事先訂適用／反例案例與通過條件，保留原版及候選結果。不能拿同一份訓練案例同時證明泛化。
- 定時執行只能觸發上述工作；啟用 skill 與 confirmed 不由時鐘決定。
