import pytest
from src.practice_2025_03_24.most_frequent_char import most_frequent_char

def test_basic():
    assert most_frequent_char("hello") == "l"

def test_tie():
    assert most_frequent_char("aabb") in ["a", "b"]

def test_single():
    assert most_frequent_char("z") == "z"

def test_empty():
    with pytest.raises(IndexError):
        most_frequent_char("")
