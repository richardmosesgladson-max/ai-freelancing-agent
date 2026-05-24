"""Generate a simple freelance proposal based on skills and match score."""


def generate_proposal(skills, score):
    """Create a short, professional freelance proposal message.

    Args:
        skills (list[str]): Skills that matched the job requirements.
        score (int): Match score percentage.

    Returns:
        str: A generated proposal string.
    """
    skill_text = ", ".join(skills) if skills else "relevant technical skills"

    proposal = (
        "Hello,\n\n"
        "I am excited to apply for this freelance opportunity. "
        f"I bring experience with {skill_text}. "
        f"Based on my resume, I have a {score}% match with the job requirements.\n\n"
        "I am confident I can deliver quality work, communicate clearly, "
        "and meet your project goals on time.\n\n"
        "Thank you for considering my proposal.\n"
        "I look forward to speaking with you.\n"
    )

    return proposal
