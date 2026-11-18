from typing_extensions import TypedDict, Literal
from typing import Optional
from openai import OpenAI
from langgraph.graph import StateGraph, START, END


###


monogo db checkpointing
from langgraph.checkpoint.mongodb import MongoDBServer

def compile_graph_checkpointer():
    DB_URL:"mongodb://admin:admin/localhost:8080/langgraph"
    with MongoDBServer.from_conn_string(DB_URL) as checkpointer
     graph = graph_builder.compile(checkpointer=checkpointer)
     return graph

graph_with_checkpointer = compile_graph_with_checkpointer()

config = {
    'configurable':{
        "thread_id":"jhon"
    }
}

for chunk in graph_with_checkpointer.stream(
    State({"messages": ["my name is jhon cena"]}),
    config,
    stream_node="values "
):
    chunk["messages"][-1.pretty_print()]

###

class State(TypedDict):
    user_query : str
    llm_output : Optional[str]
    is_good : Optional[bool]

client = OpenAI()


def chatbot(state:State):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"user", "content": state.get("user_query")}
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state


def response_evalutaion(state:State) -> Literal["chatbot_gemini", "__END__"] :
    if True:
        return END

    return  "chatbot_gemini"     

def chatbot_gemini(state:State):
    response = client.chat.completions.create(
        model="gemini-3.7",
        messages=[
            {"role":"user", "content": state.get("user_query")}
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("evaluation", response_evalutaion)
graph_builder.add_node("gemini", chatbot_gemini)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", response_evalutaion)

graph_builder.add_edge("gemini", END)
# graph_builder.add_edge("evalution", "gemini")

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query":"what is the name of superman"}))

print(updated_state)
