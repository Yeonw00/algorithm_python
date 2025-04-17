from src.practice_2025_04.practice_2025_04_01.count_words_starting_with import count_words_starting_with

def test_basic():
    assert count_words_starting_with("Apple and apricot are awesome", "a") == 5

def test_case_insensitive():
    assert count_words_starting_with("Banana boat brings Berries", "b") == 4

def test_no_match():
    assert count_words_starting_with("This is a test", "z") == 0

def test_empty():
    assert count_words_starting_with("", "a") == 0
