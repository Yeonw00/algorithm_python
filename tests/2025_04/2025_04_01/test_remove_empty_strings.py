from src.practice_2025_04.practice_2025_04_01 import remove_empty_strings

def test_basic():
    assert remove_empty_strings(["a", "", "b", "", "c"]) == ["a", "b", "c"]

def test_all_empty():
    assert remove_empty_strings(["", "", ""]) == []

def test_no_empty():
    assert remove_empty_strings(["hello", "world"]) == ["hello", "world"]

def test_empty_list():
    assert remove_empty_strings([]) == []
