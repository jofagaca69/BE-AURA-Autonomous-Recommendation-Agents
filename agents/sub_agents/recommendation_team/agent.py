from google.adk.agents import LoopAgent
from .interviewer.agent import interviewer

recommendation_team = LoopAgent(
    name="recommendation_team",
    description="A team of agents that work together to provide recommendations.",
    sub_agents=[
        interviewer
    ],
    max_iterations=5
)