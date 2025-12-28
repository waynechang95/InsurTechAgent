from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """
    The shared state of the multi-agent system.
    """
    # The conversation history
    messages: List[BaseMessage]
    
    # Customer Profile Information (gathered by Sales/Data Agent)
    customer_profile: Dict[str, Any]
    
    # Candidates policies retrieved by Policy Agent
    policy_candidates: List[Dict[str, Any]]
    
    # Analysis outputs from parallel agents
    underwriting_analysis: Optional[str]
    background_analysis: Optional[str]
    risk_analysis: Optional[str]
    
    # The final "Devil's Advocate" critique
    rights_critique: Optional[str]
    
    # Final recommendation
    final_recommendation: Optional[str]

    # Flow control
    next_step: str
    revision_count: int
