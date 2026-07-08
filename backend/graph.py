from langgraph.graph import StateGraph, START, END

from state import LearningPathState

from tools.roadmap import generate_roadmap
from tools.resources import recommend_resources
from tools.projects import suggest_projects
from tools.planner import create_daily_plan


# =====================================================
# Roadmap Node
# =====================================================

def roadmap_node(state: LearningPathState):

    print("ROADMAP NODE")

    roadmap = generate_roadmap(
    state["selected_career"],
    state["matched_skills"],
    state["missing_skills"]
)

    return {
        "roadmap": roadmap
    }


# =====================================================
# Resources Node
# =====================================================

def resources_node(state: LearningPathState):

    print("RESOURCES NODE")

    resources = recommend_resources(
    state["selected_career"],
    state["missing_skills"],
    state["roadmap"]
)

    return {
        "resources": resources
    }


# =====================================================
# Projects Node
# =====================================================

def projects_node(state: LearningPathState):

    print("PROJECTS NODE")

    projects = suggest_projects(
    state["selected_career"],
    state["missing_skills"],
    state["roadmap"]
)

    return {
        "projects": projects
    }


# =====================================================
# Planner Node
# =====================================================

def planner_node(state: LearningPathState):

    print("PLANNER NODE")

    planner = create_daily_plan(
    state["selected_career"],
    state["missing_skills"],
    state["roadmap"],
    state["projects"]
) 
    state["projects"]
    

    return {
        "planner": planner
    }


# =====================================================
# Combine Node
# =====================================================

def combine_node(state: LearningPathState):

    print("COMBINING RESPONSE")

    final_response = f"""
# Personalized Learning Path

Career: {state['selected_career']}
---
## Current Skills

{", ".join(state["matched_skills"])}

---

## Skills To Learn

{", ".join(state["missing_skills"])}

---
## Learning Roadmap

{state['roadmap']}

---

## Resources

{state['resources']}

---

## Projects

{state['projects']}

---

## Study Plan

{state['planner']}
"""

    return {
        "final_response": final_response
    }


# =====================================================
# Build Graph
# =====================================================

builder = StateGraph(LearningPathState)

builder.add_node("roadmap", roadmap_node)
builder.add_node("resources", resources_node)
builder.add_node("projects", projects_node)
builder.add_node("planner", planner_node)
builder.add_node("combine", combine_node)

builder.add_edge(START, "roadmap")
builder.add_edge("roadmap", "resources")
builder.add_edge("resources", "projects")
builder.add_edge("projects", "planner")
builder.add_edge("planner", "combine")
builder.add_edge("combine", END)

graph = builder.compile()