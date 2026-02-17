from parser import extract_text
from extractor import extract_skills

text = extract_text("../sample_resume/demo.pdf")

known, other = extract_skills(text)

print("\nKNOWN SKILLS:\n", known)
print("\nOTHER WORDS:\n", other)
