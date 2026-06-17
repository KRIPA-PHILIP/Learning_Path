from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from learning_path import generate_learning_path

app = FastAPI(title="Learning Path Agent API")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Request Model
# -----------------------------
class GoalRequest(BaseModel):
    goal: str


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Learning Path Agent API Running"
    }


# -----------------------------
# Generate Learning Path
# -----------------------------
@app.post("/generate-learning-path")
def generate_learning_path_api(request: GoalRequest):

    try:

        result = generate_learning_path.invoke(
            {
                "goal": request.goal
            }
        )

        return {
            "goal": request.goal,
            "learning_path": result
        }

    except Exception as e:

        return {
            "error": str(e)
        }