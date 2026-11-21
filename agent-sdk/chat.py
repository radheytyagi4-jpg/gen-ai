from openai import Agent, runner, WebSearchTool, function_tool, Weather_agent



@function_tool
def get_weather(city:str):
    """
    fetch the weather based on city
    args:city


    """
    url=""
    response = requests.get(url)

Weather_agent = Agent(
    name="",
    instrucitons=""
)

Leader = Agent(
    name="",
    instructions="",
    tools=[
        WebSearchTool(
            name="weather_agent",
            description=""
        )
    ]
)

resultt = runner.run(Leader, "heyy")


print(resultt.final_output)
print(resultt.raw_response)

agent = Agent(
    name="",
    instruction="",
    tools=[
        WebSearchTool()
        ,
        get_weather
    ]
)

result = runner.asyn_run(agent, "inputttt")


print(result.final_output)



