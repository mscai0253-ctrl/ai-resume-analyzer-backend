from parser import extract_text
from details import extract_email, extract_phone, extract_name, extract_education, extract_experience

text = extract_text("../sample_resume/demo.pdf")

print("Name:", extract_name(text))
print("Email:", extract_email(text))
print("Phone:", extract_phone(text))
print("Education:", extract_education(text))
print("Experience:", extract_experience(text))