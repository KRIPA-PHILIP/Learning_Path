from langchain_core.tools import tool
from llm import llm


@tool
def create_daily_plan(
    goal: str,
    roadmap: str,
    projects: str
) -> str:
    """
    Create a study plan based on roadmap and projects.
    """

    print("PLANNER TOOL CALLED")

    prompt = f"""
    You are an expert study planner and career coach.

    Goal:
    {goal}

    Learning Roadmap:
    {roadmap}

    Recommended Projects:
    {projects}

    Create a practical study plan based on the roadmap and projects.

    Assume:
    - 2 hours per day
    - 6 days per week

    Return the response in the following format:

    # Daily Schedule
    - Daily learning activities
    - Recommended study hours

    # Weekly Milestones
    Week 1:
    Week 2:
    Week 3:
    ...

    # Revision Plan
    - When to revise
    - How to track progress

    # Project Schedule
    - When to start beginner projects
    - When to start intermediate projects
    - When to start advanced projects

    # Monthly Checkpoints
    - Skills to verify
    - Portfolio progress review

    # Completion Criteria
    Explain how the learner can determine they are job-ready.

    Make the schedule realistic, practical, and aligned with the roadmap and projects.
    """

    response = llm.invoke(prompt)

    return response.content