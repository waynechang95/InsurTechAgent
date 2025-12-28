import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration for vLLM
# Assuming vLLM is running locally on port 8000
# Usage: vllm serve Qwen/Qwen3-14B
VLLM_API_KEY = "EMPTY"
VLLM_API_BASE = "http://localhost:8000/v1"
MODEL_NAME = "Qwen/Qwen3-14B"  # Adjust if the serving name is different

def get_llm(temperature=0.7):
    """Returns a ChatOpenAI instance configured for the local vLLM server."""
    return ChatOpenAI(
        model=MODEL_NAME,
        openai_api_key=VLLM_API_KEY,
        openai_api_base=VLLM_API_BASE,
        temperature=temperature,
        max_tokens=2048
    )
