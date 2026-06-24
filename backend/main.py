from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph import graph
from agent import agent
from session_memory import memory


app = FastAPI(title="Learning Path Agent API")


# ==========================================================
# CORS
# ==========================================================

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


# ==========================================================
# Request Models
# ==========================================================

class GoalRequest(BaseModel):
    session_id: str
    goal: str


class ChatRequest(BaseModel):
    session_id: str
    message: str


# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():
    return {
        "message": "Learning Path Agent API Running"
    }


# ==========================================================
# Generate Learning Path
# ==========================================================

@app.post("/generate-learning-path")
def generate_learning_path(request: GoalRequest):

    try:

        print("\n" + "=" * 70)
        print("LANGGRAPH EXECUTION STARTED")
        print("Session :", request.session_id)
        print("Goal    :", request.goal)
        print("=" * 70)

        result = graph.invoke(
            {
                "goal": request.goal,
                "roadmap": "",
                "resources": "",
                "projects": "",
                "planner": "",
                "final_response": ""
            }
        )

        # Save learning path
        memory.save_learning_path(
            request.session_id,
            result["final_response"]
        )

        print("=" * 70)
        print("LEARNING PATH SAVED")
        print("Session :", request.session_id)
        print("=" * 70)

        print("=" * 70)
        print("LANGGRAPH EXECUTION COMPLETED")
        print("=" * 70)

        return {
            "session_id": request.session_id,
            "goal": request.goal,
            "learning_path": result["final_response"]
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "error": str(e)
        }


# ==========================================================
# Career Chat (DeepAgents)
# ==========================================================

@app.post("/career-chat")
def career_chat(request: ChatRequest):

    try:

        # --------------------------------------------------
        # Retrieve learning path
        # --------------------------------------------------

        learning_path = memory.get_learning_path(
            request.session_id
        )

        if not learning_path:

            return {
                "error": "No learning path found for this session. Please generate a learning path first."
            }

        # --------------------------------------------------
        # Save current user message
        # --------------------------------------------------

        memory.add_chat(
            request.session_id,
            "user",
            request.message
        )

        # --------------------------------------------------
        # Retrieve updated chat history
        # --------------------------------------------------

        chat_history = memory.get_chat_history(
            request.session_id
        )

        history_text = "\n".join(
            f"{chat['role']}: {chat['content']}"
            for chat in chat_history[-6:]
        )

        print("=" * 70)
        print("CAREER CHAT")
        print("Session :", request.session_id)
        print("=" * 70)

        # --------------------------------------------------
        # Build prompt
        # --------------------------------------------------

        prompt = f"""
You are an expert AI Career Mentor.

The user has already generated the following learning path.

========================================================

LEARNING PATH

{learning_path}

========================================================

PREVIOUS CONVERSATION

{history_text}

========================================================

CURRENT QUESTION

{request.message}

========================================================

Instructions:

- Use the learning path whenever applicable.
- Use previous conversation for context.
- Provide practical advice.
- Explain concepts clearly.
- Keep responses concise.
- Recommend improvements whenever possible.
"""

        # --------------------------------------------------
        # Invoke DeepAgent
        # --------------------------------------------------

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        response = result["messages"][-1].content

        # --------------------------------------------------
        # Save assistant response
        # --------------------------------------------------

        memory.add_chat(
            request.session_id,
            "assistant",
            response
        )

        return {
            "session_id": request.session_id,
            "response": response
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "error": str(e)
        }