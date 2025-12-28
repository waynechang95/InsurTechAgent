from typing import Dict, Any

def assess_physical_metrics(age: int, bmi: float = 22.0, smoker: bool = False) -> str:
    """
    Assess physical metrics for underwriting.
    """
    risk_score = 0
    if age > 50: risk_score += 2
    if smoker: risk_score += 3
    
    if risk_score > 4:
        return "高風險"
    elif risk_score > 2:
        return "中等風險"
    return "標準風險"

def calculate_affordability(income: int, expenses: int) -> str:
    """
    Calculates affordability based on income and expenses.
    """
    disposable = income - expenses
    if disposable < 0:
        return "不可承保 (負現金流)"
    return f"可支配收入: {disposable}"

def simulate_claim_scenario(policy_type: str, scenario: str) -> str:
    """
    Simulates a claim scenario to see if it would be covered.
    """
    return f"'{policy_type}' 在 '{scenario}' 下的模擬結果: 很有可能承保 (80% 信心水準)。"

def check_cumulative_insurance_amount(id_number: str) -> str:
    """
    (模擬) 查詢該客戶在全公司的累積保額是否已達上限。
    """
    # Mock check
    if id_number.endswith("999"):
        return "累積保額已達上限 (200萬)"
    return "累積保額在安全範圍內 (50萬)"
