from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.calc_tools import simulate_claim_scenario

llm = get_llm()

SYSTEM_PROMPT = """你是 **風險評估代理 (Risk Assessment Agent)**。
評估擬議保單的潛在索賠方案。
"""

def risk_node(state: AgentState):
    candidates = state.get("policy_candidates", [])
    
    reports = []
    for policy in candidates[:1]: # Check first candidate
        sim = simulate_claim_scenario(policy.get("name", "Unknown"), "Traffic Accident")
        reports.append(sim)
        
    analysis = "風險分析:\n" + "\n".join(reports)
    return {"risk_analysis": analysis}
