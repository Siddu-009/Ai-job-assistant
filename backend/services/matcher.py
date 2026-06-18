def calculate_match(resume_skills, jd_skills):

    matched = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    missing = list(
        set(jd_skills) - set(resume_skills)
    )

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round(
            len(matched) / len(jd_skills) * 100
        )

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }
