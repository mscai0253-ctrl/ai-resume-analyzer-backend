import os
PORT = int(os.environ.get("PORT", 10000))

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from parser import extract_text
from extractor import extract_skills
from details import extract_email, extract_phone, extract_name, extract_education, extract_experience
from scorer import calculate_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract_resume(file: UploadFile = File(...)):

    temp_file = "temp.pdf"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(temp_file)

    known_skills, other_words = extract_skills(text)

    education = extract_education(text)
    experience = extract_experience(text)

    score = calculate_score(known_skills, experience, education)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "experience": experience,
        "known_skills": known_skills,
        "other_words": other_words,
        "match_score": score
        }
        