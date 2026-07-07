import pymupdf as fitz


def extract_resume_text(file_path: str) -> str:
    """
    Extract text from a PDF resume.
    """

    try:
        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    except Exception as e:
        raise Exception(f"Failed to extract resume text: {str(e)}")