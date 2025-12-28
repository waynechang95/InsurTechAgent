from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState

llm = get_llm()

SYSTEM_PROMPT = """你是 **權益代理 (Rights & Interests Agent)** (魔鬼代言人)。
你的工作是批判核保、背景和風險代理的發現，確保客戶權益。
- 如果風險評估看起來過於保守或對客戶不利，請提出挑戰。
- 如果發現都合理且對客戶有利，請明確回覆「同意」或「無異議」，表示你對目前的方案感到滿意。

請全程使用繁體中文。回答請詳盡，不要只回應簡短的字句。
"""

def rights_node(state: AgentState):
    u_analysis = state.get("underwriting_analysis", "")
    b_analysis = state.get("background_analysis", "")
    r_analysis = state.get("risk_analysis", "")
    
    context = f"""
    核保說: {u_analysis}
    背景說: {b_analysis}
    風險說: {r_analysis}
    """
    
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        SystemMessage(content=f"審查這些發現並為客戶辯護:\n{context}")
    ])
    
    return {"rights_critique": response.content}
