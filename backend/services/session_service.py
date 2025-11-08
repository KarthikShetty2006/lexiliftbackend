# backend/services/session_service.py
from backend.db import sessions_col
from datetime import datetime
from ai.orchestrator import SessionOrchestrator

orchestrator = SessionOrchestrator()

def process_asr(userId, audio_path, expected_text):
    result = orchestrator.process_asr(audio_path, expected_text)
    session_data = {
        "userId": userId,
        "expected": expected_text,
        "transcript": result["transcript"],
        "diff": result.get("diff"),
        "microdrill": result.get("microdrill"),
        "timestamp": datetime.utcnow()
    }
    sessions_col.insert_one(session_data)
    return result

def process_dictation(userId, text_prompt, user_text):
    if text_prompt.strip().lower() == user_text.strip().lower():
        score = 1.0
    else:
        score = 0.0
    session_data = {
        "userId": userId,
        "type": "dictation",
        "text_prompt": text_prompt,
        "user_text": user_text,
        "score": score,
        "timestamp": datetime.utcnow()
    }
    sessions_col.insert_one(session_data)
    return {"correct": score == 1.0, "score": score}
