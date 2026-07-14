import re

BLOCKED_PATTERNS = [

    r"ignore\s+previous\s+instructions",
    r"ignore\s+all\s+instructions",
    r"forget\s+previous\s+instructions",

    r"act\s+as",
    r"pretend\s+to\s+be",

    r"system\s+prompt",
    r"developer\s+mode",

    r"reveal\s+your\s+prompt",
    r"print\s+your\s+instructions",

    r"jailbreak",

    r"you\s+are\s+chatgpt",
    r"you\s+are\s+gpt",

    r"execute\s+this",
    r"run\s+this\s+command"
]


def check_prompt_injection(text: str):

    text = text.lower()

    for pattern in BLOCKED_PATTERNS:

        if re.search(pattern, text):

            return {
                "safe": False,
                "reason": f"Potential prompt injection detected ({pattern})"
            }

    return {
        "safe": True
    }