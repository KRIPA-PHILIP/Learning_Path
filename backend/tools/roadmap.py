from llm import llm


def generate_roadmap(
    selected_career: str,
    matched_skills: list,
    missing_skills: list
) -> str:
    """
    Generate a personalized learning roadmap.
    """

    print("ROADMAP TOOL CALLED")

    prompt = f"""
You are an expert Career Mentor.

The learner wants to become:

{selected_career}

Current Skills:

{', '.join(matched_skills)}

Skills to Learn:

{', '.join(missing_skills)}

IMPORTANT INSTRUCTIONS:

- The learner already knows the current skills.
- DO NOT include topics that are already known.
- Focus ONLY on the missing skills.
- Arrange the learning path from beginner to advanced.
- Make it industry-oriented.

Generate the roadmap with the following sections:

# Prerequisites

# Beginner Phase

# Intermediate Phase

# Advanced Phase

# Timeline

Rules:

- Maximum 5 bullet points per section.
- Keep explanations concise.
- Use Markdown.
- Avoid unnecessary theory.
- Prioritize practical learning.
"""

    response = llm.invoke(prompt)

    return response.content