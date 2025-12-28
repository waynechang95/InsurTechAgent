import sys
import os
from langchain_core.messages import HumanMessage
from src.graph.workflow import create_graph

# Ensure src is in python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

def main():
    print("正在初始化Agentic AI 團隊...")
    app = create_graph()
    
    print("歡迎來到保險代理系統。")
    user_input = input("使用者: ")
    if not user_input:
        user_input = "您好，我今年 35 歲，是一名上班族。最近身邊有朋友生病住院，讓我開始重視醫療保險。我的預算大概每個月 3000 元左右，想要有基本的住院和手術保障。請問有什麼適合的方案嗎？"
    
    initial_state = {
        "messages": [HumanMessage(content=user_input)],
        "customer_profile": {},
        "policy_candidates": []
    }
    
    print("\n--- 處理中 (這可能需要一點時間) ---")
    

    # Stream the graph events
    for event in app.stream(initial_state):
        for node_name, node_output in event.items():
            print(f"\n[節點完成: {node_name}]")
            if "rights_critique" in node_output:
                print(f"權益代理評論: {node_output['rights_critique'][:]}")
            if "messages" in node_output:
                print(f"代理輸出: {node_output['messages'][-1].content[:]}")

    print("\n--- 工作流程完成 ---")

if __name__ == "__main__":
    main()
