from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
    temperature=0
)


def validate_resume(resume_text: str):

    prompt = f"""
You are an expert document classifier.

Your task is to determine whether the following document is a RESUME/CV.

A valid resume usually contains some of the following:

- Candidate Name
- Education
- Skills
- Experience
- Projects
- Certifications
- Contact Information

If the document is NOT a resume
(example: insurance certificate, invoice, bank statement, passport, marksheet, bill, contract, research paper, etc.), return false.

Return ONLY valid JSON.

{{
    "is_resume": true,
    "reason": "Short reason"
}}

OR

{{
    "is_resume": false,
    "reason": "Short reason"
}}

Document:

{resume_text}
"""

    response = llm.invoke(prompt)

    return json.loads(response.content)