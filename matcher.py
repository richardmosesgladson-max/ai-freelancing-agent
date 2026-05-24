"""Match freelancer resume skills to job post requirements."""


def calculate_match(resume_skills, job_skills):
    """Compare resume skills with job skills and compute a match percentage.

    Args:
        resume_skills (list[str]): Skills found in the resume.
        job_skills (list[str]): Skills required by the job post.

    Returns:
        dict: A dictionary with score, matched skills, and missing skills.
    """
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched_skills = sorted(resume_set & job_set)
    missing_skills = sorted(job_set - resume_set)

    total_required = len(job_skills)
    if total_required == 0:
        score = 0
    else:
        score = int((len(matched_skills) / total_required) * 100)

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }
