from langchain_core.tools import tool
from llm import llm


@tool
def suggest_projects(goal: str, roadmap: str) -> str:
    """
    Suggest projects aligned with the learning roadmap.
    """

    print("PROJECTS TOOL CALLED")

    prompt = f"""
You are a software mentor.

Career Goal:

{goal}

Roadmap:

{roadmap}

Suggest:

## Beginner
2 projects

## Intermediate
2 projects

## Advanced
1 project

For each project provide:

- Name
- Objective
- Skills Learned

Rules:

- Maximum 3 lines per project.
- Use Markdown.
"""

    response = llm.invoke(prompt)

    return response.content