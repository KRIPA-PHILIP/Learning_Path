from langchain_core.tools import tool

from tools.roadmap import generate_roadmap
from tools.resources import recommend_resources
from tools.projects import suggest_projects
from tools.planner import create_daily_plan


@tool
def generate_learning_path(goal: str):
    """
    Generate a complete learning path including roadmap,
    resources, projects and study plan.
    """

    print("LEARNING PATH TOOL CALLED")

    roadmap = generate_roadmap.invoke(
        {"goal": goal}
    )

    resources = recommend_resources.invoke(
        {"goal": goal}
    )

    projects = suggest_projects.invoke(
        {"goal": goal}
    )

    planner = create_daily_plan.invoke(
        {"goal": goal}
    )

    return f"""
# ROADMAP

{roadmap}

# RESOURCES

{resources}

# PROJECTS

{projects}

# DAILY PLAN

{planner}
"""