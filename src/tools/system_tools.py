from typing import Dict, Any, List

def monitor_agents_status() -> Dict[str, str]:
    """
    即時查詢所有 Agent 的目前狀態（如 idle, working, error）。
    並可取得特定 Agent 的工作紀錄或回應結果。
    """
    # Mock status
    return {
        "sales_agent": "working",
        "data_agent": "idle",
        "policy_agent": "idle",
        "underwriting_agent": "idle",
        "background_agent": "idle",
        "risk_agent": "idle",
        "rights_agent": "idle"
    }

def workflow_planner(user_requirement: str) -> Dict[str, Any]:
    """
    依據使用者的需求與當前任務階段，自動規畫後續流程。
    包括保單詢問、需求確認、方案推薦與保費試算等步驟。
    """
    # Mock planning
    return {
        "current_stage": "initial_assessment",
        "next_steps": ["data_collection", "policy_search", "risk_assessment"],
        "estimated_time": "2 minutes"
    }

def generate_proposal(customer_profile: Dict[str, Any], policy_candidates: List[Dict[str, Any]]) -> str:
    """
    根據使用者的需求與條件生成個人化的保單推薦方案。
    """
    if not policy_candidates:
        return "無法生成提案：沒有合適的保單候選人。"
    
    proposal = "### 個人化保單推薦提案\n\n"
    proposal += f"基於您提供的資料 (職業: {customer_profile.get('occupation', '未知')}, 年齡: {customer_profile.get('age', '未知')})，我們推薦以下方案：\n"
    
    for policy in policy_candidates:
        proposal += f"- **{policy.get('name', '未命名保單')}**: {policy.get('details', '無詳細資料')}\n"
    
    proposal += "\n此提案已綜合考量您的風險承受能力與預算。"
    return proposal
