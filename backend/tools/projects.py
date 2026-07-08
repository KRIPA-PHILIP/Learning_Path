from llm import llm


def suggest_projects(
    selected_career: str,
    missing_skills: list,
    roadmap: str
) -> str:
    """
    Suggest personalized portfolio projects based on the
    learner's missing skills and roadmap.
    """

    print("PROJECTS TOOL CALLED")

    prompt = f"""
You are an expert software engineering mentor.

The learner wants to become:

{selected_career}

The learner wants to become:

{selected_career}

Missing Skills:

{', '.join(missing_skills)}

Learning Roadmap:

{roadmap}

Design portfolio projects that help the learner master the missing skills.

Generate:

# Beginner Projects
- 3 projects

# Intermediate Projects
- 3 projects

# Advanced Projects
- 2 projects

For every project include:

- Project Name
- Technologies Used
- Skills Covered
- One-line Description

Rules:

- Projects must progressively increase in difficulty.
- Focus on industry-relevant projects.
- Every project should help improve one or more missing skills.
- Return in Markdown format.
"""

    response = llm.invoke(prompt)

    return response.content