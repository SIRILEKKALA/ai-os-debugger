import re

COMMON_FIXES = {
    "ModuteNotroundrError": "ModuleNotFoundError",
    "ModuteNotFoundError": "ModuleNotFoundError",
    "tFoundError": "ModuleNotFoundError",
}

def clean_ocr_text(text: str) -> str:
    # Normalize whitespace
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    # Fix common OCR mistakes
    for wrong, correct in COMMON_FIXES.items():
        text = re.sub(wrong, correct, text, flags=re.IGNORECASE)

    return text.strip()

def extract_error(text: str) -> str | None:
    match = re.search(
        r"(ModuleNotFoundError:\s*No module named\s*['\"~]?([a-zA-Z0-9_]+))",
        text
    )
    if match:
        error_line = match.group(1)
        error_line = error_line.replace("~", "")
        return error_line

    return None