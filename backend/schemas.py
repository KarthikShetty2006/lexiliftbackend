# backend/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class AssessmentStart(BaseModel):
    userId: str
    age: int

class AssessmentSubmit(BaseModel):
    userId: str
    results: dict

class ExerciseGenerate(BaseModel):
    userId: str
    age: int
    subtype_confusions: Optional[List[str]] = None

class ASRRequest(BaseModel):
    userId: str
    expected_text: str

class DictationRequest(BaseModel):
    userId: str
    text_prompt: str
    user_text: str
