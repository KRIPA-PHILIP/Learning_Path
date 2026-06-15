from langchain_core.tools import tool
from llm import llm

@tool
def recommend_resources(
    goal: str,
    roadmap: str
) -> str:
    """
    Recommend learning resources based on the roadmap.
    """

    print("RESOURCES TOOL CALLED")

    prompt = f"""
    Goal:
    {goal}

    Roadmap:
    {roadmap}

    Recommend resources specifically for the roadmap above.

    Return the response in the following format:

    # Beginner Resources
    - Official Documentation
    - Free Courses
    - YouTube Channels
    - Practice Platforms

    # Intermediate Resources
    - Official Documentation
    - Free Courses
    - YouTube Channels
    - Practice Platforms

    # Advanced Resources
    - Official Documentation
    - Paid Courses
    - Books
    - Practice Platforms

    For every resource include:
    - Resource Name
    - Why it is useful
    - Recommended phase to use it

    Prioritize industry-recognized and up-to-date resources.
    """

    response = llm.invoke(prompt)

    return response.content