#You are going to type this 3 times 

#1st time 
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage # The foundation class for all message types in LangGraph
from langchain_core.messages import ToolMessage
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tool_node 

# 1. define state
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 2. define tools
@tool
def add(a: int, b:int):
    """ This is an addition function that adds 2 numbers together"""

    return a + b

@tool
def subtract(a:int, b: int):
    """subtraction function"""

    return a-b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a*b

tools = [add, subtract, multiply]
model = ChatOllama(model="qwen3.5:9b").bind_tools(tools)



# ======================== from here we are not familiar ========================



# 3. define graph nodes and conditional logic 
def model_call(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content=
        "you are my AI assistant, please answer my query to the best of your ability."
                                  )
    response = model.invoke([system_prompt] + state["messages"])

    return {"messages": [response]}


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls: 
        return "end"
    else:
        return "continue"


# 4. construct graph
graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools= tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent", 
    should_continue,
    {"continue": "tools",
     "end": END
     },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()

def print_stream(stream):
    for s in stream:
        #this line did not understand 
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else: 
            message.pretty_print()


inputs = {"messages": [("user", "add 40 + 12 and then multiply the result by 3. Also tell me a joke please.")]}
print_stream(app.stream(inputs, stream_mode="values"))

app
