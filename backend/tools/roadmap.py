from langchain_core.tools import tool
from llm import llm

@tool
def generate_roadmap(goal: str) -> str:
    """
    Generate a detailed learning roadmap.
    """

    print("ROADMAP TOOL CALLED")

    prompt = f"""
    Create a detailed roadmap for becoming a {goal}.

    Include:
    - Month-wise plan
    - Topics to learn
    - Learning order
    """

    response = llm.invoke(prompt)

    return response.content