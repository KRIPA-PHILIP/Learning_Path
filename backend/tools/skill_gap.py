def generate_skill_gap(candidate_skills, required_skills):
    """
    Compare candidate skills with required skills.
    """

    # Convert everything to lowercase for comparison
    candidate_lower = {skill.lower(): skill for skill in candidate_skills}
    required_lower = {skill.lower(): skill for skill in required_skills}

    matched = []
    missing = []

    for skill in required_lower:

        if skill in candidate_lower:
            matched.append(required_lower[skill])
        else:
            missing.append(required_lower[skill])

    match_percentage = 0

    if len(required_skills) > 0:
        match_percentage = round(
            (len(matched) / len(required_skills)) * 100
        )

    return {

        "matched_skills": matched,

        "missing_skills": missing,

        "match_percentage": match_percentage

    }