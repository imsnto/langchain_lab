from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent, create_tool_calling_agent
from langchain.prompts import PromptTemplate
from llms.llms import llm

from settings.settings import weather_api_key, weather_url
import requests

def calculator(expression):
    """Evaluate a basic arithmetic expression (e.g. '5 + 3', '10 * 2')."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def get_weather(location):
    """Get the current/real-time weather for a given location."""
    try:
        params = {
            'appid': weather_api_key,
            'q': location,
            'units': 'metric', # Use 'imperial' for Farhenheit
        }
        response =  requests.get(weather_url, params=params)
        if response.status_code == 200:
            data =  response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            return f"Weather in {location}: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%"
        else:
            return f"Error fetching weather data: {response.status_code}"
    except Exception as e:
        return f"Error fetching weather data: {e}"

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Use this to evaluate basic arithmetic expressions like '5 + 3' or '10 * 2'.\
                    Input must be a valid math expression."
    ),
    Tool(
        name="Weather",
        func=get_weather,
        description="Use this to get the current weather for a given location like 'Dhaka', or 'New York'.\
                    Input must be a valid city name"
    )
]

# Define the ReAct agent prompt
react_prompt = PromptTemplate.from_template(
    """Disclaimer: Never use brave_search. 
    Answer the following questions as best as you can. You have access to the following tools:
    {{tools}}
    Use the following format:
    Question: {input}
    Thought: [your reasoning]
    Action: [tool name, exactly as it appears above]
    Action Input: [Input to the tool] 
    Observation: [result from the tool]
    ... (repeat Thought/Action/Observation as needed)
    Final Answer: [your final answer]
        
    If you don't need a tool, provide the answer directly. Begin!
    
    Question: {input}
    {agent_scratchpad}
    {{tool_names}}
    """
)

# # Create the ReAct agent
# agent = create_react_agent(
#     llm = llm,
#     tools = tools,
#     prompt = react_prompt
# )

# Construct the Tools agent
agent = create_tool_calling_agent(llm, tools, react_prompt)

# Create the AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test the agent with a math question
question = "What is 5*3 + 3*45?"
question = "Current weather of Dhaka now?"
response = agent_executor.invoke({"input": question})
print(f"Response: {response["output"]}")
