from llm import llm


def suggest_projects(goal: str, roadmap: str) -> str:
    """
    Suggest portfolio projects based on the roadmap.
    """

    print("PROJECTS TOOL CALLED")

    prompt = f"""
You are an expert software mentor.

Career Goal:

{goal}

Learning Roadmap:

{roadmap}

Suggest:

## Beginner Projects
- 3 Projects

## Intermediate Projects
- 3 Projects

## Advanced Projects
- 2 Projects

Rules:

- Mention technologies.
- One line explanation.
- Return Markdown.
"""

    response = llm.invoke(prompt)

    return response.content