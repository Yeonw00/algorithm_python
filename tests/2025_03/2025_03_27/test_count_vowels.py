from src.practice_2025_03.practice_2025_03_27.count_vowels import count_vowels

def test_basic():
    assert count_vowels("Hello World") == 3

def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_empty():
    assert count_vowels("") == 0
