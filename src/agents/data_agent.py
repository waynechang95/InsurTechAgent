from langchain_core.messages import SystemMessage
from ..config import get_llm
from ..graph.state import AgentState
from ..tools.pii_tools import extract_and_verify_pii, generate_application_json
from ..tools.rag_tools import get_form_schema

llm = get_llm()

SYSTEM_PROMPT = """你是 **資料收集代理 (Data Collection Agent)**。
你的任務是從對話中提取資料，並將其整理為標準格式。

可用工具：
- `extract_and_verify_pii`: 提取並驗證 PII。
- `get_form_schema`: 獲取特定產品的表單欄位需求。
- `generate_application_json`: 生成標準要保書 JSON。

請以 JSON 格式輸出提取的使用者資料。
"""

def data_node(state: AgentState):
    messages = state["messages"]
    
    # Simulate workflow:
    # 1. Get Schema (mock assumes Life Insurance for now)
    schema = get_form_schema("Life Insurance")
    
    # 2. Extract Data
    conversation_text = "\n".join([m.content for m in messages])
    field_pairs = extract_and_verify_pii(conversation_text)
    
    # 3. Generate JSON
    application_json = generate_application_json(field_pairs)
    
    # Assuming profile_data matches application structure for this demo
    return {"customer_profile": application_json["data"]}
