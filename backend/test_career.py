from resume.extractor import extract_resume_text
from tools.resume_analysis import analyze_resume
from tools.career_recommendation import recommend_careers

resume_text = extract_resume_text("sample_resume.pdf")

profile = analyze_resume(resume_text)

careers = recommend_careers(profile)

print(careers)