from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message:str
    pass


def greeting_node(state: AgentState) -> AgentState:
    "Simple node that add a simple message to the state"
    print(state)
    state['msg'] = "Hey " + state["name"] + ",your age is "+ state["age"]
    return state

graph=StateGraph(AgentState)

graph.add_node("greeter",greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")


app=graph.compile()
from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))
message={"name":"Nikhil","age":25}
result=app.invoke(message)
print(result["name"])

