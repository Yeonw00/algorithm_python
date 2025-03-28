from src.practice_2025_03_28.find_longest_word import find_longest_word

def test_basic():
    assert find_longest_word("The quick brown fox") == "quick"

def test_multiple_longest():
    assert find_longest_word("I love Python Java") == "Python"

def test_single_word():
    assert find_longest_word("Supercalifragilisticexpialidocious") == "Supercalifragilisticexpialidocious"

def test_empty():
    assert find_longest_word("") == ""
