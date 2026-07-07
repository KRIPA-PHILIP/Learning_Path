from resume.extractor import extract_resume_text
from tools.resume_validator import validate_resume

text = extract_resume_text("sample_resume.pdf")

result = validate_resume(text)

print(result)