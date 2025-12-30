from text_validation import validate_text

def test_empty_text():
    valid, msg = validate_text("")
    assert valid is False

def test_short_text():
    valid, msg = validate_text("Hi")
    assert valid is False

def test_valid_text():
    valid, cleaned = validate_text("Hello World!")
    assert valid is True
    assert cleaned == "Hello World!"

def test_special_characters():
    valid, cleaned = validate_text("Hello @#$ World")
    assert valid is True
    assert cleaned == "Hello  World"
