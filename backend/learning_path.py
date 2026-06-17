from langchain_core.tools import tool

from tools.roadmap import generate_roadmap
from tools.resources import recommend_resources
from tools.projects import suggest_projects
from tools.planner import create_daily_plan


@tool
def generate_learning_path(goal: str):
    """
    Generate a complete learning path including roadmap,
    resources, projects, and study plan.
    """

    print("LEARNING PATH TOOL CALLED")

    try:
        # Step 1: Generate Roadmap
        roadmap = generate_roadmap.invoke(
            {"goal": goal}
        )
        print("ROADMAP GENERATED")

        # Step 2: Generate Resources using Roadmap
        resources = recommend_resources.invoke(
            {
                "goal": goal,
                "roadmap": roadmap
            }
        )
        print("RESOURCES GENERATED")

        # Step 3: Generate Projects using Roadmap
        projects = suggest_projects.invoke(
            {
                "goal": goal,
                "roadmap": roadmap
            }
        )
        print("PROJECTS GENERATED")

        # Step 4: Generate Study Plan using Roadmap + Projects
        planner = create_daily_plan.invoke(
            {
                "goal": goal,
                "roadmap": roadmap,
                "projects": projects
            }
        )
        print("PLANNER GENERATED")

        return f"""
# Learning Path for {goal}

## Learning Roadmap

{roadmap}

## Learning Resources

{resources}

## Practice Projects

{projects}

## Study Plan

{planner}

## Final Recommendation

Follow the roadmap sequentially and complete projects alongside each learning phase. Focus on consistent practice, regular revision, and portfolio development to maximize learning outcomes.
"""

    except Exception as e:
        return f"Error generating learning path: {str(e)}"