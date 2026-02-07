from fastapi import FastAPI
from backend.ai_engine import generate_lesson

app = FastAPI(title="EduPulse AI Backend")

@app.get("/")
def home():
    return {"message": "EduPulse AI Backend Running"}

@app.post("/lesson")
def lesson(title: str, level: str):
    return generate_lesson(title, level)
