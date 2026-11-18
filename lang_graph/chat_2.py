from typing_extensions import TypedDict, Literal
from typing import Optional
from openai import OpenAI
from langgraph.graph import StateGraph, START, END

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
