from src.practice_2025_03.practice_2025_03_27.count_words import count_words

def test_case_1():
    assert count_words("Hello world") == 2

def test_case_2():
    text = "The quick brown fox jumps over the lazy dog"
    assert count_words(text) == 9

def test_empty():
    assert count_words("") == 0

def test_multiple_spaces():
    assert count_words("   too   many   spaces   ") == 3

