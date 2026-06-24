from llm import llm


def recommend_resources(goal: str, roadmap: str) -> str:
    """
    Recommend learning resources based on the roadmap.
    """

    print("RESOURCES TOOL CALLED")

    prompt = f"""
You are an expert technical mentor.

Career Goal:

{goal}

Learning Roadmap:

{roadmap}

Recommend ONLY:

## Documentation
- 3 official documentation websites

## YouTube
- 3 YouTube channels

## Courses
- 2 online courses

## Books
- 2 recommended books

Rules:

- One line description only.
- Avoid long explanations.
- Return in Markdown.
"""

    response = llm.invoke(prompt)

    return response.content