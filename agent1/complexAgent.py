import random
from typing import TypedDict, List
from langgraph.graph import START , END
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    name: str
    number:List[int]
    counter:int

def greeting_node(state: AgentState) -> AgentState:
    "This will return the name of user"
    state['name']=f"Hi {state['name']}, how are you?"
    print(state)
    state["counter"]=0
    return state


def random_node(state:AgentState) -> AgentState:
    print(state)
    state["number"].append(random.randint(0,10))
    state["counter"]+=1
    print(state)
    return state

def should_continue(state:AgentState) -> AgentState:
    if(state["counter"]<5):
        print("Entering the loop")
        print(state["number"])
        return "loop"
    else:
        return "exit"

graph=StateGraph(AgentState)

graph.add_node("greeting", greeting_node)

graph.add_node("random",random_node)

graph.add_edge("greeting","random")

graph.set_entry_point("greeting")

graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop":"random",
        "exit": END
    }
)
app=graph.compile()

app.invoke({"name": "nikhil", "number":[],"counter": 1})
