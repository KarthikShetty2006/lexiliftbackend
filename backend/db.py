# backend/db.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "lexilift")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users_col = db["users"]
assessments_col = db["assessments"]
exercises_col = db["exercises"]
sessions_col = db["sessions"]
analytics_col = db["analytics"]
