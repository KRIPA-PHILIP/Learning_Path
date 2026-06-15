from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class GoalRequest(BaseModel):
    goal: str

@app.get("/")
def home():
    return {"message": "Learning Path Agent API Running"}

@app.post("/generate-learning-path")
def generate_learning_path(request: GoalRequest):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    I want to become a {request.goal}.

                    Generate:
                    - Learning Roadmap
                    - Resources
                    - Projects
                    - Daily Study Plan
                    """
                }
            ]
        }
    )

    return {
        "goal": request.goal,
        "learning_path": result["messages"][-1].content
    }