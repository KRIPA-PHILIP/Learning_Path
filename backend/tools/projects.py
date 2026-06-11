from langchain_core.tools import tool
from llm import llm

@tool
def suggest_projects(goal: str) -> str:
    """
    Suggest projects for practice.
    """

    print("PROJECTS TOOL CALLED")

    prompt = f"""
    Suggest beginner, intermediate and advanced projects
    for becoming a {goal}.
    """

    response = llm.invoke(prompt)

    return response.content