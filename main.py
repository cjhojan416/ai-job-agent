from fastapi import FastAPI
from app.routes.cv_routes import router as cv_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
print("OPENROUTER:", os.getenv("OPENROUTER_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(cv_router)


@app.get("/")
def home():
    return {"message": "AI Job Agent running"}

