from typing import Dict, Any

def extract_and_verify_pii(conversation_text: str) -> Dict[str, Any]:
    """
    Extracts PII (Personally Identifiable Information) from the conversation 
    and verifies it against required fields.
    """
    # In a real system, this might use an LLM extraction chain or regex
    # Mocking extraction
    extracted_data = {
        "age": 30,  # Mock
        "occupation": "工程師", # Mock
        "medical_history": "無", # Mock
        "budget": "高"  # Mock
    }
    return extracted_data

def generate_application_json(field_value_pairs: Dict[str, Any]) -> Dict[str, Any]:
    """
    將收集到的零散欄位組裝成標準的要保書 JSON 物件。
    """
    application = {
        "application_type": "Standard",
        "data": field_value_pairs,
        "status": "Draft",
        "validation": "Passed"
    }
    return application
