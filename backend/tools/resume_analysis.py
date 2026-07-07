import json

from llm import llm


def analyze_resume(resume_text: str):

    prompt = f"""
You are an expert Resume Analyzer.

Analyze the resume and return ONLY valid JSON.

Extract:

1. Full Name
2. Education
3. Experience
4. Skills
5. Projects
6. Certifications (if available)

Return ONLY JSON.

Example:

{{
    "name":"",
    "education":"",
    "experience":"",
    "skills":[],
    "projects":[],
    "certifications":[]
}}

Resume:

{resume_text}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)

    except Exception:
        return {
            "error": "Unable to parse response.",
            "raw_response": response.content
        }