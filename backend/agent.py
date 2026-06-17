from dotenv import load_dotenv
import os

from deepagents import create_deep_agent

from learning_path import generate_learning_path

load_dotenv()

agent = create_deep_agent(
    model=f"ollama:{os.getenv('OLLAMA_MODEL')}",
    tools=[
        generate_learning_path
    ],
)