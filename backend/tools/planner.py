from llm import llm


def create_daily_plan(
    selected_career: str,
    missing_skills: list,
    roadmap: str,
    projects: str
) -> str:
    """
    Generate a personalized weekly study plan.
    """

    print("PLANNER TOOL CALLED")

    prompt = f"""
You are an expert Career Coach and Study Planner.

The learner wants to become:

{selected_career}

Missing Skills:

{', '.join(missing_skills)}

Learning Roadmap:

{roadmap}

Projects:

{projects}

Create a practical weekly learning schedule.

Include:

# Weekly Plan

- Week 1
- Week 2
- Week 3
- Week 4

For each week mention:

- Topics to Learn
- Hands-on Practice
- Project Work
- Revision

Finally include:

# Daily Study Schedule

# Revision Strategy

# Practice Tips

Rules:

- Prioritize the missing skills.
- Balance theory and practical work.
- Keep the schedule realistic.
- Use Markdown formatting.
"""

    response = llm.invoke(prompt)

    return response.content