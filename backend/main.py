import os
import ssl
import nltk
import shutil
from tempfile import NamedTemporaryFile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_text
from extractor import extract_skills
from details import extract_email, extract_phone, extract_name, extract_education, extract_experience
from scorer import calculate_score

# ------------------- NLTK SETUP -------------------
try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except:
    pass


# ------------------- FASTAPI -------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- API -------------------
@app.post("/extract")
async def extract_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Please upload a PDF file")

    temp_path = None

    try:
        # Save uploaded file safely
        with NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            shutil.copyfileobj(file.file, temp)
            temp_path = temp.name

        # Extract text from PDF
        text = extract_text(temp_path)

        if not text or len(text.strip()) < 20:
            raise HTTPException(status_code=400, detail="Could not read text from PDF")

        # Process resume
        known_skills, other_words = extract_skills(text)
        education = extract_education(text)
        experience = extract_experience(text)

        score = calculate_score(known_skills, experience, education)

        return {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "education": education,
            "experience": experience,
            "known_skills": known_skills,
            "other_words": other_words,
            "match_score": score
        }

    except Exception as e:
        # This prevents 500 crash and shows real error
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # cleanup temp file
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
