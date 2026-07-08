from typing import TypedDict


class LearningPathState(TypedDict):

    # Career Information
    selected_career: str

    # Skill Gap
    matched_skills: list[str]

    missing_skills: list[str]

    # LangGraph Nodes
    roadmap: str

    resources: str

    projects: str

    planner: str

    # Final Response
    final_response: str