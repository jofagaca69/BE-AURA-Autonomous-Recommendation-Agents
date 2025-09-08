import os

from dotenv import load_dotenv
from google.adk import Agent

from . import prompt
from agents.tools.appendToState import append_to_state

load_dotenv()

greeter = Agent(
    name='Greeter',
    model=os.getenv("MODEL_NAME"),
    description='Greeter agent',
    instruction=prompt.GREETING_AGENT_PROMPT,
    tools=[append_to_state]
)