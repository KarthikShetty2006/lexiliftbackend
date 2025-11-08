# backend/services/assessment_service.py
from backend.db import assessments_col
from datetime import datetime

def start_assessment(userId, age):
    assessment = {
        "userId": userId,
        "age": age,
        "startedAt": datetime.utcnow(),
        "status": "in_progress"
    }
    assessments_col.insert_one(assessment)
    return {"message": "Assessment started", "assessmentId": str(assessment["_id"])}

def submit_assessment(userId, results):
    assessments_col.update_one({"userId": userId}, {"$set": {"results": results, "completedAt": datetime.utcnow(), "status": "completed"}})
    return {"message": "Assessment submitted"}
