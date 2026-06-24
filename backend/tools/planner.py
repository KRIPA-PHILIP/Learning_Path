from llm import llm


def create_daily_plan(goal: str, roadmap: str, projects: str) -> str:
    """
    Create a study planner based on roadmap and projects.
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

Create:

## Weekly Plan

## Daily Schedule

## Revision Strategy

## Practice Tips

Rules:

- Keep it concise.
- Use Markdown.
"""

    response = llm.invoke(prompt)

    return response.content