
from dotenv import load_dotenv
import os
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
# from pydantic import BaseModel

load_dotenv()
api_key3= os.getenv("GENAI_API_KEY")
# api_key2 = os.getenv("ANTHROPIC_API_KEY")
# api_key = os.getenv("OPEN_AI_KEY")

# try:
#     llm = ChatOpenAI(
#     model_name="gpt-4o",
#     api_key=api_key
#     )

#     response = llm.invoke("hello, how's you?")
#     print(response.content)

# except Exception as e:
#     print(f"error while generating response :  {e}")




# try:
#     llm2 = ChatAnthropic(
#     model="claude-3-5-sonnet-20241022",
#     api_key=api_key2
#     )

#     response = llm2.invoke("Hello, how are you?")

#     print(response.content) 

# except Exception as e:
#     print (f"An error occurred: {e}") 

try:
    while True:
        user_query = input("ask..")
        llm3 = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        api_key=api_key3
        )

        response = llm3.invoke(user_query)
        print(response.text)
except Exception as e:
    print(f"error while generating response : {e}")