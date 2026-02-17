from parser import extract_text

text = extract_text("../sample_resume/demo.pdf")
print("\n---------RESUME TEXT---------\n")
print(text[:1000])