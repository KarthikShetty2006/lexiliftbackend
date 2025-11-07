from fastapi import FastAPI
from db import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase

app = FastAPI(title="LexiLift Backend", version="1.0")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/db-test")
async def test_db():
    try:
        db: AsyncIOMotorDatabase = await get_db()
        collections = await db.list_collection_names()
        return {"connected": True, "collections": collections}
    except Exception as e:
        return {"connected": False, "error": str(e)}
