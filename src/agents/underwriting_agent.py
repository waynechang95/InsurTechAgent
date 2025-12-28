from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.calc_tools import assess_physical_metrics, check_cumulative_insurance_amount
from ..tools.rag_tools import query_underwriting_guidelines

llm = get_llm()

SYSTEM_PROMPT = """你是 **核保代理 (Underwriting Agent)**。
你的任務是進行「預核保」初篩，比對健康告知事項與除外責任。

可用工具：
- `assess_physical_metrics`: 計算體況等級。
- `check_cumulative_insurance_amount`: 查詢累積保額。
- `query_underwriting_guidelines`: 查詢具體核保準則。
"""

def underwriting_node(state: AgentState):
    profile = state.get("customer_profile", {})
    
    # 1. Assess Physical Metrics
    risk_level = assess_physical_metrics(
        age=profile.get("age", 40),
        smoker=str(profile.get("medical_history", "")).lower() == "smoker"
    )
    
    # 2. Check Guidelines (mock disease)
    guideline = query_underwriting_guidelines("High Blood Pressure", "Medical Insurance")
    
    # 3. Check Cumulative Amount
    cumulative_status = check_cumulative_insurance_amount(str(profile.get("id_number", "A123456789")))
    
    analysis = f"核保評估: 病患是 {risk_level}。{cumulative_status}。\n參考準則: {guideline}"
    return {"underwriting_analysis": analysis}
