# backend/services/analytics_service.py
from backend.db import sessions_col
from datetime import datetime, timedelta

def get_user_progress(userId):
    last_10_days = datetime.utcnow() - timedelta(days=10)
    sessions = list(sessions_col.find({"userId": userId, "timestamp": {"$gte": last_10_days}}))
    
    total_sessions = len(sessions)
    correct_sessions = len([s for s in sessions if s.get("score", 0) == 1.0])
    accuracy = (correct_sessions / total_sessions) * 100 if total_sessions > 0 else 0

    return {
        "total_sessions": total_sessions,
        "accuracy": accuracy,
        "recent_sessions": sessions[-5:]
    }
