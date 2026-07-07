import json

from llm import llm


def recommend_careers(candidate_profile: dict):
    """
    Recommend the top 3 career paths based on the candidate profile.
    """

    prompt = f"""
You are an experienced Career Advisor.

Based on the candidate profile below, recommend the TOP 3 most suitable careers.

For each career provide:

- title
- confidence (0-100)
- reason

Return ONLY valid JSON.

Output format:

{{
    "recommended_careers":[
        {{
            "title":"",
            "confidence":0,
            "reason":"",
            "required_skills":[]
        }}
    ]
}}

Candidate Profile:

{json.dumps(candidate_profile, indent=2)}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown if present
    if content.startswith("```"):
        lines = content.splitlines()
        content = "\n".join(lines[1:-1])

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid JSON returned by LLM.",
            "raw_output": content
        }