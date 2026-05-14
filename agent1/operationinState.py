import math
from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    values:List[int]
    operation:str
    result :str


def processing_node(state: AgentState) -> AgentState:
    "Simple node that handle multiple key values to the state"
    print(state)
    if state["operation"] == "+":
        state['result'] = f"Hey {state["name"]} , your answer is  {sum(state["values"])}"
    elif state["operation"] =="*":
        state['result'] = f"Hey {state["name"]} , your answer is  {math.prod(state["values"])}"
    else:
        state["result"]="Invalid"
    return state

graph=StateGraph(AgentState)

graph.add_node("processor",processing_node)
graph.set_entry_point("processor")
graph.set_finish_point("processor")


app=graph.compile()
answers = app.invoke({"name": "Nikhil Goyal","values": [1,2,3,4] , "operation": "-"})
response=app.invoke(answers)
print(response["result"])

