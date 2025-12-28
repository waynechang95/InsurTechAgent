from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.rag_tools import rag_query, get_policy_details, analyze_insurance_rules

llm = get_llm()

SYSTEM_PROMPT = """你是 **保單資料代理 (Policy Data Agent)**。
你的任務是管理公司現有的保單方案，提供專業建議。

可用工具：
- `get_policy_details`: 取得保單詳細資訊。
- `rag_query`: 語義搜尋保單文件。
- `analyze_insurance_rules`: 分析承保與投保規則。
"""

def policy_node(state: AgentState):
    profile = state.get("customer_profile", {})
    # Formulate a query based on profile
    query = f"適合職業 {profile.get('occupation', '未知')} 年齡 {profile.get('age', '未知')} 的保單"
    
    # 1. Search policies
    candidates = rag_query(query)
    
    # 2. Analyze rules (mock)
    rule_analysis = analyze_insurance_rules(f"年齡 {profile.get('age')}")
    
    # In a real app, we might parse this into structured dicts
    params = [{"name": c[:20], "details": c + f" ({rule_analysis})"} for c in candidates]
    
    return {"policy_candidates": params}
