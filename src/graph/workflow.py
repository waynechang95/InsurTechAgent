from langgraph.graph import StateGraph, END
from .state import AgentState

# Import Agent Nodes
from ..agents.sales_agent import sales_node
from ..agents.data_agent import data_node
from ..agents.policy_agent import policy_node
from ..agents.underwriting_agent import underwriting_node
from ..agents.background_agent import background_node
from ..agents.risk_agent import risk_node
from ..agents.rights_agent import rights_node

def create_graph():
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("sales", sales_node)
    workflow.add_node("data_collection", data_node)
    
    # The "Diamond" Middle Layer
    workflow.add_node("policy", policy_node)
    workflow.add_node("underwriting", underwriting_node)
    workflow.add_node("background", background_node)
    workflow.add_node("risk", risk_node)
    
    # Convergence
    workflow.add_node("rights", rights_node)

    # Define Edges
    
    # 1. Start interaction with Sales
    workflow.set_entry_point("sales")
    
    # Router logic from Sales
    def should_continue(state):
        # Decision made by Sales Agent
        next_step = state.get("next_step")
        
        if next_step == "refine":
            return "data_collection" # or policy, depending on what needs refinement
        if next_step == "end" or state.get("final_recommendation"):
            return END
            
        # Default flow for initial interaction
        if state.get("rights_critique"):
             # checks if we just came from rights but Sales logic didn't catch it for some reason
             # Fallback to end to prevent infinite loop if logic fails
             return END
             
        return "data_collection"

    workflow.add_conditional_edges(
        "sales",
        should_continue,
        {
            "data_collection": "data_collection",
            END: END
        }
    )
    
    # 2. Data -> Fan Out to Experts
    workflow.add_edge("data_collection", "policy")
    workflow.add_edge("data_collection", "underwriting")
    workflow.add_edge("data_collection", "background")
    workflow.add_edge("data_collection", "risk")
    
    # 3. Experts -> Converge on Rights Agent
    workflow.add_edge("policy", "rights")
    workflow.add_edge("underwriting", "rights")
    workflow.add_edge("background", "rights")
    workflow.add_edge("risk", "rights")
    
    # 4. Rights -> Sales (Closing Loop)
    # The Rights agent critiques. Then Sales needs to see it.
    # We'll just end at Rights for this simplified "generation" request or pass back to Sales?
    # Let's pass back to Sales to "Finalize".
    workflow.add_edge("rights", "sales")

    return workflow.compile()
