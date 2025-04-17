from src.practice_2025_03.practice_2025_03_28.capitalize_words import capitalize_words

def test_basic():
    assert capitalize_words("hello world") == "Hello World"

def test_mixed_case():
    assert capitalize_words("hELLo WoRLD") == "Hello World"

def test_single_word():
    assert capitalize_words("python") == "Python"

def test_empty():
    assert capitalize_words("") == ""
