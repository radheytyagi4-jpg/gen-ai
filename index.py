from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()
api_key3= os.getenv("GENAI_API_KEY")


class ResearchResponse(BaseModel):
    topic:str
    summary:str
    source:list[str]
    tools_used:list[str]

llm = ChatGoogleGenerativeAI(
model="gemini-3.8-flash",
api_key=api_key3
)


parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
          """
          you are a research assistant that will help generate a research paper.
          Answer the user query and use nessecary tools.
          Wrap the output this is format and provide no other text \n{format_instructions}
          """),
          ("placeholder", "{chat_history}"),
          ("human", "{query}"),
          ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent= create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)

agent_executor=AgentExecutor(agent=agent, tools=[], verbose=True)

# try:
#     while True:
#         user_query = input("ask..")

#         response = llm3.invoke(user_query)
#         print(response.text)

# except Exception as e:
#     print(f"error while generating response : {e}")

raw_response = agent_executor.invoke({"query": "what is the capital of France?"})

print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print(f"Error parsing response: {e}")
