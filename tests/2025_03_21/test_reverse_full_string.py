from src.practice_2025_03_21.reverse_full_string import reverse_string

def test_reverse_basic():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("abc123") == "321cba"

def test_reverse_palindrome():
    assert reverse_string("madam") == "madam"  # 회문일 경우

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_with_spaces():
    assert reverse_string(" hello world ") == " dlrow olleh "

def test_reverse_special_chars():
    assert reverse_string("!@#123") == "321#@!"