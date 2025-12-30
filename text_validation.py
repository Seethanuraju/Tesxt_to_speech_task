import re

def validate_text(text):
    if not text or text.strip() == "":
        return False, "Text cannot be empty."

    cleaned_text = re.sub(r"[^\w\s.,!?]", "", text)

    if len(cleaned_text.strip()) < 3:
        return False, "Text is too short."

    return True, cleaned_text
