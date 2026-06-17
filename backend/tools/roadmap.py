from langchain_core.tools import tool
from llm import llm


@tool
def generate_roadmap(goal: str) -> str:
    """
    Generate a concise learning roadmap for a career goal.
    """

    print("ROADMAP TOOL CALLED")

    prompt = f"""
You are an expert career mentor.

Create a concise learning roadmap for becoming a {goal}.

Include ONLY:

1. Prerequisites
2. Beginner Phase
3. Intermediate Phase
4. Advanced Phase
5. Estimated Timeline

Rules:

- Maximum 5 bullet points per section.
- Keep explanations short.
- Use Markdown headings.
- Do not add unnecessary details.
"""

    response = llm.invoke(prompt)

    return response.content