import nltk
import os

# download required NLTK data on server startup
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except:
    pass


import os
PORT = int(os.environ.get("PORT", 10000))

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from parser import extract_text
from extractor import extract_skills
from details import extract_email, extract_phone, extract_name, extract_education, extract_experience
from scorer import calculate_score
from tempfile import NamedTemporaryFile

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

    # create unique temp file
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        shutil.copyfileobj(file.file, temp)
        temp_path = temp.name

    text = extract_text(temp_path)

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