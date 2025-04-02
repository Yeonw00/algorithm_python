from src.practice_2025_04_02.most_frequent_element import most_frequent_element

def test_basic():
    assert most_frequent_element([1, 3, 1, 3, 2, 1]) == 1

def test_first_appearance_priority():
    assert most_frequent_element([4, 5, 5, 4, 4, 5]) == 4  # both 4 and 5 appear 3 times

def test_single_element():
    assert most_frequent_element([7]) == 7

def test_all_unique():
    assert most_frequent_element([10, 20, 30]) == 10
