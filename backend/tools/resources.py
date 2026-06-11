from langchain_core.tools import tool
from llm import llm

@tool
def recommend_resources(goal: str) -> str:
    """
    Recommend courses, books, docs and YouTube channels.
    """

    print("RESOURCES TOOL CALLED")

    prompt = f"""
    Recommend learning resources for becoming a {goal}.

    Include:
    - Courses
    - Documentation
    - YouTube channels
    - Books
    """

    response = llm.invoke(prompt)

    return response.content