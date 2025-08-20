from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Explicit state schema
class AgentState(TypedDict):
    input: str
    output: str

# Node function
def echo_node(state: AgentState):
    llm = ChatOpenAI(
        model_name="gpt-4",
        openai_api_key=openai_api_key
    )
    resp = llm.invoke(state["input"])
    return {"output": resp.content}

# Define graph
workflow = StateGraph(AgentState)
workflow.add_node("echo", echo_node)
workflow.set_entry_point("echo")
workflow.set_finish_point("echo")

# Compile graph
graph = workflow.compile()
