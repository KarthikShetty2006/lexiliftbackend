from fastapi import FastAPI
from app.routes import dummy_routes

app = FastAPI(title="LexiLift Backend")

app.include_router(dummy_routes.router)

@app.get("/")
def root():
    return {"msg": "LexiLift backend running!"}
