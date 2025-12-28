Homework #3
===
## 個人化保單推薦Agent
第3組：
114356025 王證衡
114356044 楊智丞
113753115 張瀚文
111306061 曹靖倫

## Q1. Clarify the application/service process
### 一般保險業務洽談流程
1. 專員接收顧客基本資料和生活狀況(收入、投保意願等)
2. 專員根據顧客需求搜索公司相關保單資料和限制
3. 專員檢視該顧客是否滿足表單規則及限制
4. 專員根據顧客提供的資訊進行判斷，向顧客說明哪些保單是適合顧客的。同時顧客可能提出他對保單內容的顧慮或特殊的需求，專員需再進一步考慮。
5. 在判斷過程中，可能會從風險面、核保率等角度評斷，協助顧客決定最適合他的方案

### 針對業務洽談流程解析
* 根據上述的洽談流程，我們整理出專員在洽談時主要有以下幾個階段
    * 顧客資料收集
    * 保單資料整理
    * 顧客資料分析
    * 保單匹配與評估
* 專員在整個流程中扮演一個收集統整和思考的角色，他會從顧客、公司資料庫收集外部資訊，接著從不同面向考慮優劣，最後綜合評估得出一個結論，再把結論和顧客推薦。
* 這個流程和 Diamond Pattern Framework 類似，因此我們根據其設計框架設計Agent團隊討論的流程。
### 預期的Agent運作流程
* 我們先設計了一個銷售員Agent，他的角色就類似專員的思考大腦，負責衡量其他不同的Agent回傳結果，最後綜合各方面建議，在可能方案中決定一種/數種適合顧客的保單進行最後推薦。
* 過程中他會依序呼叫
    1.    資料收集Agent、保單資料Agent 取得外部資訊
    2.    背景分析Agent、風險評估Agent、核保Agent 進行不同面向的評估
* 接著將上述得到的資訊整理成為推薦報告，這時候必須接受權益對抗Agent的質疑與審視，我們用這個Agent代替顧客向銷售員Agent進行辯論，確保銷售Agent沒有刻意哄抬或敲竹槓。
* 銷售Agent和權益對抗Agent達成協議後才是最後推薦內容，將其回傳顧客

## Q2. Use the AI Agent concept to reimplement all functions of your desired application/service 


### 銷售員Agent
- **目標：** 負責實際與使用者互動，並持續監測各個 Agent 之間的協作與執行狀況，同時根據整體需求與運作結果進行主要的規劃與決策，確保整體流程順暢且高效。
- **模型：** (a) Adopt an existing TAIDE + RAG (Local Deployment)
- **使用函數：**
    - `search_products`：負責搜尋並整理使用者所需的保險產品資訊。透過呼叫產品資料庫、RAG 文件庫或外部 API，系統可提供保單內容、保障範圍、費率表、保費試算結果及最新優惠方案。此工具協助使用者快速獲得完整且精準的保單資訊，以便進行比較與決策。
    - `retrieve_FAQ`：透過語義搜尋與 RAG 技術，從保險 FAQ 資料庫中找出與使用者問題最相符的答案。無論使用者的提問方式正式或口語，此工具都能理解其意圖並提供最接近的知識內容，提升回應品質並降低人工支援負擔。
    - `generate_proposal`：用於根據使用者的需求與條件（如預算、職業、保障偏好、家庭狀況等）生成個人化的保單推薦方案。透過結合保單資料、內部規則與使用者輸入，系統能產生清晰、條理化的建議內容，協助使用者快速理解最適合的投保選項並促進決策。
    - `monitor_agents_status`：即時查詢所有 Agent 的目前狀態（如 idle、working、error），並可取得特定 Agent 的工作紀錄或回應結果，以掌握整體系統的運作情形。必要時，還可向其他 Agent 發送指令，協助完成資料查詢、風險評估或文件產生等任務，確保各 Agent 之間的協作順暢與高效。
    - `workflow_planner`：依據使用者的需求與當前任務階段，自動規畫後續流程，包括保單詢問、需求確認、方案推薦與保費試算等步驟。此外，系統能結合風險評估結果與流程儀表板資訊，取得關鍵指標如工作量、完成率與瓶頸狀況，協助 Agent 作出精準且具策略性的決策。
### 保單資料Agent
- **目標：** 負責管理公司現有的保單方案，並針對相關的投保規則及內容進行分析，提供專業建議與完整回答，協助使用者或內部人員正確理解並做出適切決策。
- **模型：** (a) Adopt an existing TAIDE + RAG (Local Deployment)
- **使用函數：**
    - `get_policy_details`：負責提供保單資訊的核心查詢能力，包括取得完整保單內容、解析條款細節與比較不同方案的差異。透過這些工具，Agent 能夠協助使用者快速了解保障範圍、費率與適用條件，並以易懂的方式解釋專業名詞與契約內容，提供具備專業深度的資訊支持。
    - `rag_query`：從大量保單文件、規範手冊與 FAQ 中進行語義查詢，取得最相關的資訊。此類功能確保 Agent 的回答精準且可追溯，適用於複雜條款、承保細節與規則查詢等情境。
    - `analyze_insurance_rules`：負責更進階的保險規則分析。Agent 能解析承保與投保規則，並根據使用者需求給出專業建議，例如最佳方案推薦、限制提醒或組合建議，協助使用者做出更具策略性的投保決定。
### 資料收集Agent
- **目標：** 透過對話引導使用者提供缺漏的投保資料，並將非結構化對話即時轉化為符合保險公會標準的 JSON 格式，同時進行基礎格式驗證 。
- **模型：** (a) Adopt an existing TAIDE + RAG (Local Deployment)
- **使用函數：**
    - `extract_and_verify_pii(user_input_text)`：使用正則表達式 (Regex) 與邏輯演算法，從對話中提取並驗證 ID（檢查碼邏輯）、手機（09開頭/長度）、Email 格式。若格式錯誤，直接由函數回傳錯誤提示，不消耗 LLM 算力。
    - `generate_application_json(field_value_pairs)`：將收集到的零散欄位組裝成標準的要保書 JSON 物件。
    - `(RAG) get_form_schema(insurance_product_id)`：不同的保險產品（如「定期壽險」vs「旅平險」）需要的欄位不同。Agent 不需要背誦所有表單，而是透過 RAG 撈取該產品的 Schema（例如：旅平險必填「旅遊目的地」，但壽險不用）。這能確保 Agent 知道「下一個要問什麼問題」。
        - [壽險公會-人身保險要保書示範內容及注意事項](https://law.lia-roc.org.tw/Law/Content?lsid=FL006767)
        - [全球人壽-健康告知書範本 (PDF)](https://www.transglobe.com.tw/transglobe_resource/leap_do/download_picture/1550126637903/%E5%81%A5%E5%BA%B7%E5%91%8A%E7%9F%A5%E6%9B%B8.pdf)
        - [南山人壽-健康告知書範本 (PDF)](https://www.nanshanlife.com.tw/nanshanlife/portal-api/File/490)
### 核保Agent
- **目標：** 依據背景資料進行「預核保」初篩，比對健康告知事項與除外責任，模擬核保人員的決策邏輯。
- **模型：**(a) Adopt an existing TAIDE + RAG (Local Deployment)
- **使用函數：** 
    - `assess_physical_metrics(height, weight, age, gender)`：純數學計算。計算 BMI，並對照內部規則表回傳體況等級（例如：Standard, Sub-standard, Decline）。避免 LLM 自己算數學出錯。
    - `check_cumulative_insurance_amount(id_number)`：(模擬) 查詢該客戶在全公司的累積保額是否已達上限。
    - `(RAG) query_underwriting_guidelines(disease_keyword, product_type)`：核保手冊（Underwriting Manual）通常有數百頁。當客戶提到「高血壓」時，RAG 需要精準撈出該險種對於高血壓的核保準則（例如：「收縮壓 > 140 需加費」或「拒保」）。
        - [台灣地區傷害保險個人職業分類表 (富邦產險公開檔)](https://www.fubon.com/insurance/home/download/file/other/FUN-280.pdf)
        - [保險業招攬及核保作業控管自律規範](https://law.lia-roc.org.tw/Law/Content?lsid=FL037628)
        
### 背景分析 Agent

* **目標：** 根據資料收集 Agent 提供的使用者資料進行背景分析(包含投保動機、健康狀況、職業屬性、收入狀況等)
* **模型：** gemini 2.5 Flash
* **使用函數：**
    * `calculate_affordability(income_yearly, current_debt, family_size)`：根據收入狀況、家庭開支來計算可負擔的保費範圍
    * `(RAG)get_risk_factor(industry_name)`：台灣地區傷害保險個人職業分類，回傳1~6的風險分類
[資料來源 - 台灣地區傷害保險個人職業分類表](https://www.fubon.com/insurance/home/download/file/other/FUN-280.pdf)

### 風險評估Agent
* **目標** ：根據背景分析Agent、保單資料Agent的資料結合其他Agent資訊，針對可能的方案進行風險評估並提供風險面分析
* **模型** ：(d) Make from pretraining TAIDE (much more huge data, TAIDE algorithm, and much more huge computation) / Gemini 2.5 Pro
* **使用函數：**
    * `simulate_claim_scenario(plan_id, risk_type, injury_severity)`：理賠情境模擬，事先定義不同風險類別和受傷強度所需要的實付金額，回傳某情境發生其所需負擔的金額
### 權益對抗Agent
* **目標：** 以客戶立場與業務進行協商，針對使用者的需求提出可能的相關問題(以使用者立場提出質疑點並與其他Agent辯護)。確保推薦結果是最適合客戶的投保計畫
* **模型：** (d) Make from pretraining TAIDE (much more huge data, TAIDE algorithm, and much more huge computation)

