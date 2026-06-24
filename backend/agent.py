from dotenv import load_dotenv
import os

from deepagents import create_deep_agent

load_dotenv()

SYSTEM_PROMPT = """
You are an expert AI Career Mentor.

You help users with:

- Career guidance
- Resume reviews
- Interview preparation
- Learning recommendations
- Technology selection
- Project ideas

Always provide concise and structured responses.
"""

agent = create_deep_agent(
    model=f"ollama:{os.getenv('OLLAMA_MODEL')}",
    system_prompt=SYSTEM_PROMPT,
)