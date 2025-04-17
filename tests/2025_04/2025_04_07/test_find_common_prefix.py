from src.practice_2025_04.practice_2025_04_07 import find_common_prefix

def test_basic():
    assert find_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_no_common():
    assert find_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_word():
    assert find_common_prefix(["hello"]) == "hello"

def test_empty_list():
    assert find_common_prefix([]) == ""
