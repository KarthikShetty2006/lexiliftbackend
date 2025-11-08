# backend/services/exercise_service.py
from backend.db import exercises_col
from datetime import datetime
from ai.generator import generate_exercises

def generate_personalized_exercises(userId, age, subtype_confusions):
    data = generate_exercises(age, subtype_confusions)
    exercises_doc = {
        "userId": userId,
        "age": age,
        "createdAt": datetime.utcnow(),
        "exercises": data
    }
    exercises_col.insert_one(exercises_doc)
    return data
