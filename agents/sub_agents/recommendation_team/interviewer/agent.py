import os
from dotenv import load_dotenv
from google.adk import Agent

from agents.tools.appendToState import append_to_state
from . import prompt

load_dotenv()

interviewer = Agent(
    name='Interviewer',
    model=os.getenv("MODEL_NAME"),
    description='An agent that interviews the user to gather information for making recommendations.',
    instruction=prompt.INTERVIEWER_AGENT_PROMPT,
    tools=[append_to_state]
)