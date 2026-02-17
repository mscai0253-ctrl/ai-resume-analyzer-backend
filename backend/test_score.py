from parser import extract_text
from extractor import extract_skills
from details import extract_education, extract_experience
from scorer import calculate_score

text = extract_text("../sample_resume/demo.pdf")

skills, other = extract_skills(text)
edu = extract_education(text)
exp = extract_experience(text)

score = calculate_score(skills, exp, edu)

print("Candidate Score:", score, "%")