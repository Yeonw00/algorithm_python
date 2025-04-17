from src.practice_2025_03.practice_2025_03_24 import palindrome_check

def test_even_length_palindrome():
    assert palindrome_check("abba")

def test_odd_length_palindrome():
    assert palindrome_check("racecar")

def test_not_palindrome():
    assert not palindrome_check("hello")

def test_single_character():
    assert palindrome_check("a")

def test_empty_string():
    assert palindrome_check("")

def test_mixed_case():
    assert not palindrome_check("RaceCar")

def test_numeric_string():
    assert palindrome_check("12321")

def test_special_characters():
    assert palindrome_check("!@##@!")
