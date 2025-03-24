from src.practice_2025_03_21.reverse_with_spacing import reverse_with_spacing

def test_basic_word():
    assert reverse_with_spacing("hello") == "o l l e h"
    assert reverse_with_spacing("abc") == "c b a"

def test_with_space_inside():
    assert reverse_with_spacing("a b") == "b   a"

def test_single_char():
    assert reverse_with_spacing("X") == "X"

def test_empty_string():
    assert reverse_with_spacing("") == ""