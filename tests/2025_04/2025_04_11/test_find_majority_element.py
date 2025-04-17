from src.practice_2025_04.practice_2025_04_11.find_majority_element import find_majority_element

def test_basic():
    assert find_majority_element([3, 3, 4, 2, 3, 3, 3]) == 3

def test_all_same():
    assert find_majority_element([2, 2, 2, 2]) == 2

def test_large_input():
    assert find_majority_element([1]*50 + [2]*49) == 1
