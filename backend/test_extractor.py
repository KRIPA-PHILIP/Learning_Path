from resume.extractor import extract_resume_text

text = extract_resume_text("sample_03_workers.pdf")

print("=" * 80)
print("EXTRACTED TEXT")
print("=" * 80)
print(text)
print("=" * 80)