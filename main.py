from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4o",
    )

llm2 = ChatAnthropic(
    model="claude-3.0",
    )