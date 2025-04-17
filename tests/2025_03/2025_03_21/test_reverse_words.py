from src.practice_2025_03.practice_2025_03_21 import reverse_words

def test_reverse_basic():
    assert reverse_words("I love Python") == "Python love I"

def test_reverse_single_word():
    assert reverse_words("Hello") == "Hello"

def test_reverse_empty():
    assert reverse_words("") == ""