from langchain_core.tools import tool
from llm import llm


@tool
def create_daily_plan(goal: str, roadmap: str, projects: str) -> str:
    """
    Generate a concise 7-day study plan.
    """

    print("PLANNER TOOL CALLED")

    prompt = f"""
You are an expert study planner.

Career Goal:

{goal}

Roadmap:

{roadmap}

Projects:

{projects}

Create a concise 7-day study plan.

Each day should contain:

- Topics
- Practice Task
- Study Time

Rules:

- Maximum 3 bullet points per day.
- Keep responses concise.
- Use Markdown.
"""

    response = llm.invoke(prompt)

    return response.content