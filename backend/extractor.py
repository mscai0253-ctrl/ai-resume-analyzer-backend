import nltk
import os

nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_path, exist_ok=True)

nltk.download("punkt", download_dir=nltk_data_path)
nltk.download("stopwords", download_dir=nltk_data_path)

nltk.data.path.append(nltk_data_path)

import re 
from skills import SKILLS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words('english'))

def extract_skills(text):

    text = text.lower()


    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    found = list(set(found))

    words = word_tokenize(text)
    words = [w for w in words if w.isalpha() and w not in STOPWORDS and len(w) > 2]

    other = []
    for w in words:
        if w not in found and w not in SKILLS:
            if re.search(r'[a-z]', w):
                other.append(w)
    other = list(set(other)) [:20]

    return found, other