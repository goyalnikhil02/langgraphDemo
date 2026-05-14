from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    age:int
    result :str


def processing_node(state: AgentState) -> AgentState:
    "Simple node that handle multiple key values to the state"
    print(state)
    state['result'] = f"Hey {state["name"]} , your age is  {state["age"]}"
    print(state)
    return state

graph=StateGraph(AgentState)

graph.add_node("processor",processing_node)
graph.set_entry_point("processor")
graph.set_finish_point("processor")


app=graph.compile()
message={"name":"Nikhil","age":25}
response=app.invoke(message)
print(response["result"])

