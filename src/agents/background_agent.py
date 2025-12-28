from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.calc_tools import calculate_affordability
from ..tools.rag_tools import get_risk_factor

llm = get_llm()

SYSTEM_PROMPT = """你是 **背景分析代理 (Background Analysis Agent)**。
你的任務是根據資料進行背景分析(包含投保動機、健康狀況、職業屬性、收入狀況等)。

可用工具：
- `calculate_affordability`: 計算可負擔保費範圍。
- `get_risk_factor`: 查詢職業風險等級 (1-6級)。
"""

def background_node(state: AgentState):
    profile = state.get("customer_profile", {})
    
    # Mock income/expense data since our tool stub didn't output it
    # In real flow, DataAgent would populate this
    income = 50000
    expenses = 30000
    
    affordability = calculate_affordability(income, expenses)
    
    # Check occupation risk
    occupation = profile.get('occupation', 'office')
    risk_level = get_risk_factor(str(occupation))
    
    analysis = f"財務背景: {affordability}。職業: {occupation} (風險等級: {risk_level})。"
    return {"background_analysis": analysis}
