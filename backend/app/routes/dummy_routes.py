from fastapi import APIRouter
from app.utils.dummy_data import dummy_user, dummy_assessment, dummy_exercise, dummy_drill

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/user")
def get_user():
    return dummy_user

@router.get("/assessment/start")
def start_assessment():
    return dummy_assessment

@router.get("/exercise/generate")
def generate_exercise():
    return dummy_exercise

@router.get("/microdrill/generate")
def generate_drill():
    return dummy_drill
