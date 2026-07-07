from tools.skill_gap import generate_skill_gap

candidate_skills = [

    "Python",

    "FastAPI",

    "SQL"

]

required_skills = [

    "Python",

    "FastAPI",

    "SQL",

    "Docker",

    "Redis",

    "Git",

    "AWS",

    "CI/CD"

]

result = generate_skill_gap(

    candidate_skills,

    required_skills

)

print(result)