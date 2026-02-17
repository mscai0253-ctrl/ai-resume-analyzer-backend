REQUIRED_SKILLS = ["python", "javascript", "react", "node", "mongodb", "api", "sql"]

def skill_score(found_skills):
    matched = len(set(found_skills) & set(REQUIRED_SKILLS))
    return (matched / len(REQUIRED_SKILLS)) * 60

def experience_score(experience):

    if not experience:
        return 0 

    text = " ".join(experience)

    if "year" in text:
        return 25
    elif "month" in text:
        return 15
    else:
        return 5

def education_score(education):

    if not education:
        return 0 
    
    text = " ".join(education).lower()

    if "msc" in text or "mtech" in text:
        return 15
    elif "bsc" in text or "btech" in text:
        return 10
    else:
        return 5

def calculate_score(skills,exp,edu):
    total = skill_score(skills) + experience_score(exp) + education_score(edu)
    return round(min(total,100), 2)
    
  