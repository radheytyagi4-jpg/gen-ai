from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

response = init_chat_model(
    model="gpt-4",
    model_provider="openai"
)


class State(TypedDict):
    messages : Annotated[list, add_messages]


#creating the nodes
def chatbot(state:State):

    llm = response.invoke(state.get("messages"))
    # print(f"\n\n\n Inside the chatbot node : {state}")
    return { "messages":"This is winters" }

def sample(state:State):

    print(f"\n\n\n Inside the sample node : {state}")
    return { "messages":"This is a sample message"}

graph_builder = StateGraph(State)

#adding the nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample", sample)


#link the edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample")
graph_builder.add_edge("sample", END)


graph = graph_builder.compile()


updated_graph = graph.invoke({"messages":[ "Hi, My name is radhey"]})

print("\n\n\n", updated_graph)