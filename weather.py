import os
from openai import OpenAI
from dotenv import load_dotenv
import requests 

load_dotenv()

api_key=os.getenv("OPEN_AI_KEY")

SYSTEM_PROMPT = """You are a helpful assistant that provides weather information.
You can provide the current weather for any city in the world.
You work on START, PLAN, OUTPUT, STEPS.
You need to first plan, plan can be bullet points, then you need to output the answer in a code block, and finally you need to provide steps to get the answer.
You can use a tool if required from the list of available tools.

Rules:
Only run one step at a time.

OUTPUT_FORMAT:
{"step":"START" | "PLAN" | "OUTPUT" | "TOOL",  "content":"string", "tool":"string", "input":"string"}

AVAILABLE_TOOLS:
    -get_weather : Takes city name as input and returns the current weather information about the city.
"""
available_tools = {
    "weather_tool":get_weather
}

def get_weather(city:str):
    url=f"https://wttr.in/{city}?format=%C+%t"
    result =requests.get(url)


    if(result.status_code==200):
        return f"The weather in {city} is : {result.text}"
    else:
        return f"Could not retrieve weather data for {city}. Please try again later."

client = OpenAI(api_key=api_key)

def main():
    user_query = input(">")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"user", "content":user_query}
        ]
    )

    print(response.choices[0].message.content)

main()