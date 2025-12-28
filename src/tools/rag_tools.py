from typing import List, Dict, Any

def retrieve_FAQ(query: str) -> str:
    """
    Retrieves FAQ answers based on the user's query.
    Mock implementation.
    """
    return f"查詢 '{query}' 的 FAQ 結果。(這是模擬回答)。"

def get_policy_details(policy_id: str) -> Dict[str, Any]:
    """
    Retrieves detailed information about a specific policy.
    """
    # Mock database content
    policies = {
        "life_basic": {"name": "基本人壽保險", "coverage": "100萬新台幣", "premium": "5000/年", "details": "條款和條件適用..."},
        "medical_plus": {"name": "醫療升級版", "coverage": "住院醫療", "premium": "3000/年", "details": "涵蓋每日住院費用..."}
    }
    return policies.get(policy_id, {"error": "找不到保單"})

def rag_query(query: str, k: int = 3) -> List[str]:
    """
    Performs a RAG search on the policy vector database.
    """
    # In a real implementation, this would query FAISS/ChromaDB
    # Returning mock context chunks
    return [
        f"符合 '{query}' 的上下文片段 1: 保單 X 涵蓋意外事故。",
        f"符合 '{query}' 的上下文片段 2: 保單 Y 排除既往症。",
        f"符合 '{query}' 的上下文片段 3: 等待期為 30 天。"
    ]

def search_products(query: str) -> List[Dict[str, Any]]:
    """
    負責搜尋並整理使用者所需的保險產品資訊。
    """
    return [
        {"name": "安心意外險", "description": "針對交通事故與日常意外提供高額保障", "premium": "2000/年"},
        {"name": "樂活醫療險", "description": "涵蓋實支實付與住院日額", "premium": "4000/年"}
    ]

def analyze_insurance_rules(rule_type: str) -> str:
    """
    負責更進階的保險規則分析。Agent 能解析承保與投保規則。
    """
    return f"針對 {rule_type} 的規則分析：建議優先考慮是否有等待期限制與年齡上限。"

def get_form_schema(product_id: str) -> Dict[str, Any]:
    """
    透過 RAG 撈取該產品的 Schema（例如：旅平險必填「旅遊目的地」，但壽險不用）。
    """
    if "travel" in product_id.lower():
        return {
            "required_fields": ["destination", "start_date", "end_date", "id_number"],
            "product_type": "Travel Insurance"
        }
    return {
        "required_fields": ["occupation", "age", "medical_history", "id_number"],
        "product_type": "Life/Health Insurance"
    }

def query_underwriting_guidelines(disease_keyword: str, product_type: str) -> str:
    """
    精準撈出該險種對於特定疾病的核保準則。
    """
    return f"查詢 '{product_type}' 對於 '{disease_keyword}' 的核保準則：可能需要體檢，視數值加費或拒保。"

def get_risk_factor(industry_name: str) -> int:
    """
    台灣地區傷害保險個人職業分類，回傳1~6的風險分類。
    """
    risks = {
        "office": 1,
        "engineer": 2,
        "construction": 6,
        "driver": 4
    }
    return risks.get(industry_name.lower(), 1)
