# LearnFlow AI Backend Guide

This repository contains the backend services for LearnFlow AI, including PDF resume upload, candidate profile analysis, career selection, and learning path generation.

The main backend entry point is [learning-path-agent/backend/main.py](learning-path-agent/backend/main.py).

## Backend screenshot

The Swagger UI screenshot below shows the upload resume endpoint UI:

- [screenshots/backend/upload-resume-endpoint.png](screenshots/backend/upload-resume-endpoint.png)

## Sample resume file

A sample PDF resume is included for testing the upload endpoint:

- [learning-path-agent/backend/sample_resumes/sample_resume.pdf](learning-path-agent/backend/sample_resumes/sample_resume.pdf)

---

## 1. Prerequisites

Make sure the following are installed:

- Python 3.10+ or 3.11+
- Ollama installed and running locally

### Install Ollama

If Ollama is not installed, install it and pull the model used by the app:

```powershell
ollama serve
ollama pull qwen3:8b
```

The backend configuration is stored in [learning-path-agent/backend/.env](learning-path-agent/backend/.env).

---

## 2. Backend setup

Open a PowerShell terminal and run:

```powershell
cd C:\Users\kripa\OneDrive\Desktop\Learn_path\learning-path-agent\backend
.\venv\Scripts\Activate.ps1
```

If you need to recreate the environment, use:

```powershell
cd C:\Users\kripa\OneDrive\Desktop\Learn_path\learning-path-agent\backend
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install fastapi uvicorn python-dotenv pymupdf deepagents httpx httpcore pydantic
```

Start the backend:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

---

## 3. Backend endpoints explained

### 3.1 GET /

- Purpose: health check / API availability
- Description: returns a simple JSON message when the backend is running.
- Sample response:

```json
{
  "message": "Learning Path Agent API Running"
}
```

### 3.2 POST /upload-resume

- Purpose: upload a PDF resume and create a candidate session
- Input: one file field named `file`
- Accepted file type: PDF only
- Behavior:
  - saves the uploaded file into `uploads/`
  - extracts text from the PDF using `resume.extractor`
  - checks for prompt injection in resume text
  - validates that the document is a resume
  - analyzes the resume to build a candidate profile
  - recommends careers based on the profile
  - returns a new `session_id`
- Outputs:
  - `success` (bool)
  - `is_resume` (bool)
  - `message` (string)
  - `session_id` (string)
  - `recommended_careers` (array)

#### Example request

```powershell
curl.exe -X POST "http://127.0.0.1:8000/upload-resume" -F "file=@C:\Users\kripa\OneDrive\Desktop\Learn_path\learning-path-agent\backend\sample_resumes\sample_resume.pdf"
```

#### Expected response shape

```json
{
  "success": true,
  "is_resume": true,
  "message": "Resume uploaded and analyzed successfully.",
  "session_id": "<session-id>",
  "recommended_careers": [
    {
      "title": "...",
      "required_skills": [
        "..."
      ]
    }
  ]
}
```

#### Why it matters
Use this endpoint first. The returned `session_id` is required for `/select-career` and `/career-chat`.

### 3.3 POST /select-career

- Purpose: choose one of the recommended careers and generate a full learning path
- Input JSON body:
  - `session_id`: the session returned by `/upload-resume`
  - `career`: the exact career title selected from recommended careers
- Behavior:
  - retrieves the saved candidate profile and recommended careers for the session
  - finds the selected career object
  - computes a skill gap between current skills and career requirements
  - saves the skill gap in session memory
  - invokes the learning path graph to generate a roadmap, resources, projects, and planner
- Outputs:
  - `message`
  - `selected_career`
  - `match_percentage`
  - `matched_skills`
  - `missing_skills`
  - `learning_path`

#### Example request body

```json
{
  "session_id": "<session-id>",
  "career": "Backend Developer"
}
```

#### Example response shape

```json
{
  "message": "Career selected successfully.",
  "selected_career": "Backend Developer",
  "match_percentage": 72,
  "matched_skills": ["Python", "APIs"],
  "missing_skills": ["Docker", "Kubernetes"],
  "learning_path": "..."
}
```

### 3.4 POST /career-chat

- Purpose: ask follow-up questions about the generated learning path
- Input JSON body:
  - `session_id`: the same session used for `/select-career`
  - `message`: the user question or prompt
- Behavior:
  - retrieves the current learning path for the session
  - appends the user message to chat history
  - builds a prompt including the saved learning path and recent chat
  - invokes the AI mentor agent
  - returns a conversational response
- Outputs:
  - `session_id`
  - `response`

#### Example request body

```json
{
  "session_id": "<session-id>",
  "message": "What technical skills should I learn first?"
}
```

#### Example response shape

```json
{
  "session_id": "<session-id>",
  "response": "You should start with the fundamentals of Python, then move to APIs and backend architecture..."
}
```

---

## 4. Recommended backend test flow

1. Start the backend server.
2. Open Swagger UI at http://127.0.0.1:8000/docs.
3. Upload [learning-path-agent/backend/sample_resumes/sample_resume.pdf](learning-path-agent/backend/sample_resumes/sample_resume.pdf) via `/upload-resume`.
4. Copy the returned `session_id`.
5. Call `/select-career` with the same `session_id` and a chosen career.
6. Call `/career-chat` with the same `session_id` and a follow-up question.

---

## 5. Troubleshooting

### Backend not responding
- Make sure Ollama is running with `ollama serve`.
- Confirm the model exists with `ollama list`.
- Check that the backend is running on port 8000.

### Resume upload fails
- Make sure the file is a PDF.
- Ensure the PDF contains readable text.
- Check the backend logs for any extraction or validation errors.

### Port already in use
- If port 8000 is already occupied, stop the other process or change the port.
