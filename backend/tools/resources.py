from llm import llm


def recommend_resources(
    selected_career: str,
    missing_skills: list,
    roadmap: str
) -> str:
    """
    Recommend personalized learning resources based on
    the learner's missing skills and roadmap.
    """

    print("RESOURCES TOOL CALLED")

    prompt = f"""
You are an expert technical mentor.

The learner wants to become:

{selected_career}

Skills the learner already has are NOT to be recommended again.

Missing Skills:

{', '.join(missing_skills)}

Learning Roadmap:

{roadmap}

Recommend learning resources ONLY for the missing skills.

Provide:

# Official Documentation
- 3 official documentation websites

# YouTube Channels
- 3 high-quality YouTube channels

# Online Courses
- 2 recommended online courses

# Books
- 2 recommended books

# Practice Platforms
- 3 websites for hands-on practice

Rules:

- Recommend only trusted resources.
- Avoid duplicate recommendations.
- Keep descriptions to one line.
- Return in Markdown format.
"""

    response = llm.invoke(prompt)

    return response.content