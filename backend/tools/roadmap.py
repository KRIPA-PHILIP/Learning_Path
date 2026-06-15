from langchain_core.tools import tool
from llm import llm

@tool
def generate_roadmap(goal: str) -> str:
    """
    Generate a detailed learning roadmap for a career goal.
    """

    print("ROADMAP TOOL CALLED")

    prompt = f"""
    Create a comprehensive roadmap for becoming a {goal}.

    Include:
    - Prerequisites
    - Beginner Phase
    - Intermediate Phase
    - Advanced Phase
    - Weekly Milestones
    - Recommended Learning Order
    - Estimated Timeline

    Format the response clearly using headings and bullet points.
    """

    response = llm.invoke(prompt)

    return response.content