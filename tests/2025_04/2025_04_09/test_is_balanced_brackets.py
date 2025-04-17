from src.practice_2025_04.practice_2025_04_09 import is_balanced_brackets

def test_valid_cases():
    assert is_balanced_brackets("()[]{}") is True
    assert is_balanced_brackets("{[()]}") is True
    assert is_balanced_brackets("") is True

def test_invalid_cases():
    assert is_balanced_brackets("([)]") is False
    assert is_balanced_brackets("(((") is False
    assert is_balanced_brackets("{[}") is False
