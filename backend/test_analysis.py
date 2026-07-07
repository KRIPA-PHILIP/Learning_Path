from resume.extractor import extract_resume_text
from tools.resume_analysis import analyze_resume

text = extract_resume_text("sample_resume.pdf")

result = analyze_resume(text)

print(result)