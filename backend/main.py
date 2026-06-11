from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class LearningRequest(BaseModel):
    goal: str

@app.post("/generate-learning-path")
def generate_learning_path(data: LearningRequest):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Create a learning path for {data.goal}

                    Include:
                    1. Roadmap
                    2. Resources
                    3. Projects
                    4. Daily Study Plan
                    """
                }
            ]
        }
    )

    return {
        "goal": data.goal,
        "response": result["messages"][-1].content
    }