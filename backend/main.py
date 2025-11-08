# backend/main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.services.assessment_service import start_assessment, submit_assessment
from backend.services.exercise_service import generate_personalized_exercises
from backend.services.session_service import process_asr, process_dictation
from backend.services.analytics_service import get_user_progress
from backend.schemas import AssessmentStart, AssessmentSubmit, ExerciseGenerate, ASRRequest, DictationRequest
import shutil
import uuid
import os

app = FastAPI(title="LexiLift Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/assessment/start")
def start_assessment_api(req: AssessmentStart):
    return start_assessment(req.userId, req.age)

@app.post("/assessment/submit")
def submit_assessment_api(req: AssessmentSubmit):
    return submit_assessment(req.userId, req.results)

@app.post("/exercise/generate")
def generate_exercise_api(req: ExerciseGenerate):
    return generate_personalized_exercises(req.userId, req.age, req.subtype_confusions)

@app.post("/session/asr")
async def asr_endpoint(userId: str = Form(...), expected_text: str = Form(...), file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{uuid.uuid4()}.wav"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = process_asr(userId, file_path, expected_text)
    return result

@app.post("/session/dictation")
def dictation_endpoint(req: DictationRequest):
    return process_dictation(req.userId, req.text_prompt, req.user_text)

@app.get("/analytics/{userId}")
def analytics_api(userId: str):
    return get_user_progress(userId)
