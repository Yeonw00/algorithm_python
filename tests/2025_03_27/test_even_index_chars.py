from src.practice_2025_03_27.even_index_chars import even_index_chars

def test_case_1():
    assert even_index_chars("abcdef") == "ace"

def test_case_2():
    assert even_index_chars("Python") == "Pto"

def test_empty():
    assert even_index_chars("") == ""

def test_one_char():
    assert even_index_chars("A") == "A"

