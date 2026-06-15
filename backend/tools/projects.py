from langchain_core.tools import tool
from llm import llm


@tool
def suggest_projects(
    goal: str,
    roadmap: str
) -> str:
    """
    Suggest projects based on the learning roadmap.
    """

    print("PROJECTS TOOL CALLED")

    prompt = f"""
    You are a senior technical mentor.

    Goal:
    {goal}

    Learning Roadmap:
    {roadmap}

    Suggest projects that directly align with the skills,
    technologies, and milestones mentioned in the roadmap.

    Return the response in the following format:

    # Beginner Projects

    For each project provide:
    - Project Name
    - Objective
    - Skills Learned
    - Technologies Used
    - Difficulty
    - Estimated Duration

    # Intermediate Projects

    For each project provide:
    - Project Name
    - Objective
    - Skills Learned
    - Technologies Used
    - Difficulty
    - Estimated Duration

    # Advanced Projects

    For each project provide:
    - Project Name
    - Objective
    - Skills Learned
    - Technologies Used
    - Difficulty
    - Estimated Duration

    # Resume Impact

    Explain how these projects help build a strong portfolio
    and improve employability for this career path.

    Ensure the projects become progressively more challenging
    and follow the roadmap learning sequence.
    """

    response = llm.invoke(prompt)

    return response.content