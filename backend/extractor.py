import nltk
import os
import re

# ---- FIX: persistent nltk path ----
NLTK_DIR = "/opt/render/nltk_data"
os.makedirs(NLTK_DIR, exist_ok=True)

nltk.data.path.append(NLTK_DIR)

# download ALL tokenizer resources
nltk.download("punkt", download_dir=NLTK_DIR)
nltk.download("punkt_tab", download_dir=NLTK_DIR)
nltk.download("stopwords", download_dir=NLTK_DIR)

from skills import SKILLS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))

def extract_skills(text):

    text = text.lower()

    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    found = list(set(found))

    # tokenize safely
    words = word_tokenize(text)
    words = [w for w in words if w.isalpha() and w not in STOPWORDS and len(w) > 2]

    other = []
    for w in words:
        if w not in found and w not in SKILLS:
            if re.search(r"[a-z]", w):
                other.append(w)

    other = list(set(other))[:20]

    return found, other
