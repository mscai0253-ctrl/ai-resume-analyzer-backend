import re 

def extract_email(text):
    match = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,}\d", text)
    return match[0] if match else None

def extract_name(text):
    lines = text.split("\n")

    for line in lines[:5]:
        words = line.strip().split()


        if 2 <= len(words) <= 4:
            if not any(char.isdigit() for char in line):
                return line.strip()

    return None

def extract_education(text):
    keywords = [ "bsc", "msc", "btech", "mtech", "be", "me", "phd", "mba"]

    found = []
    for line in text.split("\n"):
        for k in keywords:
            if k in line.lower():
                found.append(line.strip())

    return list(set(found))

def extract_experience(text):
        matches = re.findall(r"\d+\+?\s*(years|months)",text.lower())
        return matches