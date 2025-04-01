from src.practice_2025_04_01.count_consonants import count_consonants

def test_basic():
    assert count_consonants("Hello") == 3

def test_all_vowels():
    assert count_consonants("aeiouAEIOU") == 0

def test_all_consonants():
    assert count_consonants("bcdfgBCDFG") == 10

def test_empty():
    assert count_consonants("") == 0
