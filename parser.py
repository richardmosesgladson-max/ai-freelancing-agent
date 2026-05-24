"""Simple resume parser for extracting technical skills."""

# A small list of skills this beginner-friendly parser can recognize.
SKILL_KEYWORDS = ["python", "fastapi", "docker", "sql", "react"]


def extract_skills(resume_text):
    """Extract known technical skills from resume text.

    Args:
        resume_text (str): The full text of a resume.

    Returns:
        list[str]: A sorted list of detected skills.
    """
    if not isinstance(resume_text, str):
        return []

    text = resume_text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found_skills.append(skill)

    return sorted(found_skills)
