"""Beginner-friendly freelancing agent that matches a resume to a job post."""

from parser import extract_skills
from matcher import calculate_match
from proposal import generate_proposal


def main():
    """Run the freelancing agent sample flow."""
    sample_resume = (
        "Experienced developer with strong Python background, building APIs with FastAPI, "
        "containerizing applications using Docker, writing SQL queries, and creating user interfaces "
        "with React."
    )

    # Example job posting requirements.
    sample_job_skills = ["Python", "FastAPI", "Docker", "SQL", "React"]

    # Extract skills from the sample resume.
    resume_skills = extract_skills(sample_resume)
    print("Extracted Skills:", resume_skills)

    # Calculate how well the resume matches the job skills.
    match_result = calculate_match(resume_skills, sample_job_skills)
    print("Match Score:", f"{match_result['score']}%")
    print("Matched Skills:", match_result["matched_skills"])
    print("Missing Skills:", match_result["missing_skills"])

    # Generate a simple proposal based on the match.
    proposal_text = generate_proposal(match_result["matched_skills"], match_result["score"])
    print("\nGenerated Proposal:\n")
    print(proposal_text)


if __name__ == "__main__":
    main()
