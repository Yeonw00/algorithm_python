from src.practice_2025_03.practice_2025_03_21.reverse_partial_string import reverse_partial_string
import pytest

def test_basic_partial_reverse():
    assert reverse_partial_string("abcdefg", 2, 5) == "abedcfg"
    assert reverse_partial_string("0123456789", 3, 7) == "0126543789"

def test_full_reverse_via_partial():
    assert reverse_partial_string("abcd", 0, 4) == "dcba"

def test_no_change_when_empty_range():
    assert reverse_partial_string("abc", 1, 1) == "abc"

def test_invalid_range():
    with pytest.raises(ValueError):
        reverse_partial_string("abcde", 4, 2)

    with pytest.raises(ValueError):
        reverse_partial_string("abcde", -1, 3)

    with pytest.raises(ValueError):
        reverse_partial_string("abcde", 0, 6)