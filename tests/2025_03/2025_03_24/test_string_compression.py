from src.practice_2025_03.practice_2025_03_24 import string_compression

def test_basic():
    assert string_compression("aaabbc") == "a3b2c1"

def test_single():
    assert string_compression("a") == "a1"

def test_empty():
    assert string_compression("") == ""
