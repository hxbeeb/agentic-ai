from dotenv import load_dotenv
import os
from phi.agent import Agent,Tool
# from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from datetime import datetime
load_dotenv()  
user_query = input("Ask the Web Agent: ")

web_agent = Agent(
    name="Web Agent",
    model=Gemini(),
    # model=Groq(id="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    instructions=[
        "Use DuckDuckGo for any online search or news-related queries.",
        "Always include sources where applicable."
    ],
    show_tool_calls=True,
    markdown=True,
)

web_agent.print_response(user_query, stream=True)
