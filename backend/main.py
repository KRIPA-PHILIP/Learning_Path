from unittest import result

from fastapi import UploadFile, File
import shutil
import os
import uuid

from httpcore import request

from tools.resume_analysis import analyze_resume
from tools.career_recommendation import recommend_careers
from session_memory import memory
from tools.skill_gap import generate_skill_gap
from tools.resume_validator import validate_resume
from resume.extractor import extract_resume_text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tools.guardrails import check_prompt_injection
from graph import graph
from agent import agent


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

class CareerSelectionRequest(BaseModel):
    session_id: str
    career: str

# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():
    return {
        "message": "Learning Path Agent API Running"
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
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:
        # --------------------------------------------------
        # Validate File Type
        # --------------------------------------------------

        if not file.filename.lower().endswith(".pdf"):

            return {

        "success": False,

        "message": "Only PDF resumes are supported."

    }
        # --------------------------------------------------
        # Create Upload Folder
        # --------------------------------------------------

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", file.filename or "resume.pdf")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # --------------------------------------------------
        # Extract Resume Text
        # --------------------------------------------------

        resume_text = extract_resume_text(file_path)
        # --------------------------------------------------
        # Prompt Injection Guard
        # --------------------------------------------------

        guard = check_prompt_injection(resume_text)

        if not guard["safe"]:

         return {

        "success": False,

        "message": guard["reason"]

    }
        # --------------------------------------------------
        # Validate Extracted Text
        # --------------------------------------------------

        if not resume_text.strip(): 

            return {

        "success": False,

        "message": "No readable text found in the uploaded PDF."

    }
        # --------------------------------------------------
        # Validate Resume
        # --------------------------------------------------

        validation = validate_resume(resume_text)

        if not validation.get("is_resume", False):
            return {
                "success": False,
                "is_resume": False,
                "message": validation.get("reason", "Uploaded document is not a resume."),
            }

        # --------------------------------------------------
        # Analyze Resume and Save Profile
        # --------------------------------------------------

        profile = analyze_resume(resume_text)
        careers = recommend_careers(profile)
        session_id = str(uuid.uuid4())
        memory.save_resume(
            session_id,
            resume_text
    )

        memory.save_candidate_profile(
            session_id,
            profile
)

        memory.save_recommended_careers(
            session_id,
            careers
)
        return {
            "success": True,
            "is_resume": True,
            "message": "Resume uploaded and analyzed successfully.",
            "session_id": session_id,
            "recommended_careers": careers,
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "error": str(e)
        }


@app.post("/select-career")
def select_career(request: CareerSelectionRequest):

    try:

        # --------------------------------------------------
        # Save Selected Career
        # --------------------------------------------------

        memory.save_selected_career(
            request.session_id,
            request.career
        )

        # --------------------------------------------------
        # Retrieve Candidate Profile
        # --------------------------------------------------

        profile = memory.get_candidate_profile(
            request.session_id
        )

        # --------------------------------------------------
        # Retrieve Recommended Careers
        # --------------------------------------------------

        careers = memory.get_recommended_careers(
            request.session_id
        )

        # --------------------------------------------------
        # Find Selected Career
        # --------------------------------------------------

        selected_career = None

        for career in careers["recommended_careers"]:

            if career["title"] == request.career:
                selected_career = career
                break

        if selected_career is None:

            return {
                "error": "Selected career not found."
            }

        # --------------------------------------------------
        # Generate Skill Gap
        # --------------------------------------------------

        skill_gap = generate_skill_gap(
            profile["skills"],
            selected_career["required_skills"]
        )

        # --------------------------------------------------
        # Save Skill Gap
        # --------------------------------------------------

        memory.save_skill_gap(
            request.session_id,
            skill_gap
        )

        # --------------------------------------------------
        # Generate Personalized Learning Path
        # --------------------------------------------------

        result = graph.invoke(
            {
                "selected_career": request.career,
                "matched_skills": skill_gap["matched_skills"],
                "missing_skills": skill_gap["missing_skills"],
                "roadmap": "",
                "resources": "",
                "projects": "",
                "planner": "",
                "final_response": ""
            }
        )

        # --------------------------------------------------
        # Save Learning Path
        # --------------------------------------------------

        memory.save_learning_path(
            request.session_id,
            result["final_response"]
        )

        # --------------------------------------------------
        # Response
        # --------------------------------------------------

        return {

            "message": "Career selected successfully.",

            "selected_career": request.career,

            "match_percentage": skill_gap["match_percentage"],

            "matched_skills": skill_gap["matched_skills"],

            "missing_skills": skill_gap["missing_skills"],

            "learning_path": result["final_response"]

        }

    except Exception as e:

        print("ERROR :", e)

        return {

            "error": str(e)

        }