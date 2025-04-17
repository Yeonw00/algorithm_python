from src.practice_2025_04.practice_2025_04_08.longest_unique_substring import longest_unique_substring

def test_example():
    assert longest_unique_substring("abcabcbb") == 3

def test_all_unique():
    assert longest_unique_substring("abcdef") == 6

def test_all_same():
    assert longest_unique_substring("aaaaaa") == 1

def test_empty():
    assert longest_unique_substring("") == 0
