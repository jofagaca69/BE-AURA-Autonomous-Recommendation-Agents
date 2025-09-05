from dotenv import load_dotenv
from google.adk.agents import SequentialAgent

from .sub_agents.greeter.agent import greeter
from .sub_agents.recommendation_team.agent import recommendation_team

load_dotenv()

main_workflow = SequentialAgent(
    name="main_worflow",
    description="Main, workflow agent",
    sub_agents=[
        greeter,
        recommendation_team
    ]
)

root_agent = main_workflow