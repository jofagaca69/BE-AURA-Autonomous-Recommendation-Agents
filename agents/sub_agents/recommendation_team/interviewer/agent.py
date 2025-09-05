import os

from dotenv import load_dotenv
from google.adk import Agent
from . import prompt

load_dotenv()

interviewer = Agent(
    name='Interviewer',
    model=os.getenv("MODEL_NAME"),
    description='An agent that interviews the user to gather information for making recommendations.',
    instruction="""
    """
)