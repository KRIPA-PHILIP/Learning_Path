from deepagents import create_deep_agent

from learning_path import generate_learning_path

from tools.roadmap import generate_roadmap
from tools.resources import recommend_resources
from tools.projects import suggest_projects
from tools.planner import create_daily_plan

agent = create_deep_agent(
    model="ollama:qwen3:8b",
    tools=[
        generate_learning_path,
        generate_roadmap,
        recommend_resources,
        suggest_projects,
        create_daily_plan
    ]
)