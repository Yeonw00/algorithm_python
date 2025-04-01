from src.practice_2025_04_01.repeat_string import repeat_string

def test_basic():
    assert repeat_string("hi", 3) == "hihihi"

def test_zero():
    assert repeat_string("abc", 0) == ""

def test_one():
    assert repeat_string("wow", 1) == "wow"

def test_empty_string():
    assert repeat_string("", 5) == ""
