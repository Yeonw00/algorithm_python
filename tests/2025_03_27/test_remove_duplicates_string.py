from src.practice_2025_03_27.remove_duplicates_string import remove_duplicates_string

def test_basic():
    assert remove_duplicates_string("banana") == "ban"

def test_all_unique():
    assert remove_duplicates_string("python") == "python"

def test_all_same():
    assert remove_duplicates_string("aaaaaa") == "a"

def test_empty():
    assert remove_duplicates_string("") == ""
