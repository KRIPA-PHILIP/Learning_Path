from langchain_core.tools import tool
from llm import llm

@tool
def create_daily_plan(goal: str) -> str:
    """
    Create a daily study schedule.
    """

    print("PLANNER TOOL CALLED")

    prompt = f"""
    Create a daily study plan for becoming a {goal}.

    Assume 2 hours per day.
    """

    response = llm.invoke(prompt)

    return response.content