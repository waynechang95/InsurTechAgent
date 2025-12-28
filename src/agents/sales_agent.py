import json
from langchain_core.messages import SystemMessage, HumanMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.rag_tools import retrieve_FAQ, search_products
from ..tools.system_tools import monitor_agents_status, workflow_planner, generate_proposal

llm = get_llm()

SYSTEM_PROMPT = """你是 **銷售代理 (Sales Agent)**，保險顧問團隊的領導者。
你的目標是與客戶互動，了解他們的需求。

功能與責任：
1. 負責實際與使用者互動，並持續監測各個 Agent 之間的協作與執行狀況。
2. 根據整體需求與運作結果進行主要的規劃與決策。

可用工具: 
- `search_products`: 搜尋保險產品資訊。
- `retrieve_FAQ`: 回答一般保險問題。
- `generate_proposal`: 生成個人化保單推薦方案 (在收集完資料後)。
- `monitor_agents_status`: 查詢 Agent 狀態。
- `workflow_planner`: 規劃後續流程。

請以中文回覆。如果你決定進入下一階段（資料收集），只需自然地輸出對話。
"""

def sales_node(state: AgentState):
    messages = state["messages"]
    critique = state.get("rights_critique")
    revision_count = state.get("revision_count", 0)
    
    # Check if we are receiving a critique from Rights Agent
    # Continue looping until revision_count hits limit OR rights agent approves
    if critique and revision_count < 5:
        
        
        # Check if critique implies approval
        # if "同意" in critique or "無異議" in critique or "滿意" in critique:
        if revision_count == 4:
             return {
                "messages": [SystemMessage(content="銷售代理: 權益代理已同意目前的方案。準備發布最終建議。")],
                "final_recommendation": f"最終方案已確認 (經過 {revision_count} 次修訂)。",
                "next_step": "end"
            }

        # Otherwise, refine
        # Sales Agent considers the critique
        prompt_with_critique = f"""
        {SYSTEM_PROMPT}

        [系統訊息]
        你收到了權益代理 (Rights Agent) 的批評：
        "{critique}"

        請根據此批評，思考如何調整方案或指示 Data Agent 收集更多資訊。
        輸出 "REFINE_PLAN" 並說明你要做的調整。
        
        目前修訂次數: {revision_count}
        """
        
        # Determine internal thought process (Simulation)
        # Using LLM to generate response to critique
        response = llm.invoke([SystemMessage(content=prompt_with_critique)] + messages)
        
        return {
            "messages": [response],
            "next_step": "refine",
            "revision_count": revision_count + 1
        }
            
    # Force finish if max revisions reached
    if revision_count >= 5:
         return {
            "messages": [SystemMessage(content="銷售代理: 已達最大修訂次數，強制定案。")],
            "final_recommendation": "最終方案產出 (強制結束)。",
            "next_step": "end"
        }

    # Normal interaction flow
    response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT)] + messages)
    
    # Simple keyword check to simulate tool usage response
    content = response.content
    if "FAQ" in content:
        ans = retrieve_FAQ(messages[-1].content)
        return {"messages": [response, SystemMessage(content=f"工具輸出: {ans}")]}
        
    return {"messages": [response]}

    return {"messages": [response]}
