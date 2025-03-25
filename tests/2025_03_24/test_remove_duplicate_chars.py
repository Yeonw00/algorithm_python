from src.practice_2025_03_24.remove_duplicate_chars import remove_duplicate_chars

def test_basic():
    assert remove_duplicate_chars("banana") == "ban"

def test_all_unique():
    assert remove_duplicate_chars("abc") == "abc"

def test_empty():
    assert remove_duplicate_chars("") == ""

def test_all_same():
    assert remove_duplicate_chars("aaaa") == "a"

def test_with_space():
    assert remove_duplicate_chars("a b a") == "a b"
