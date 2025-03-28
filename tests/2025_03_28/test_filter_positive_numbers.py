from src.practice_2025_03_28.filter_positive_numbers import filter_positive_numbers

def test_basic():
    assert filter_positive_numbers([-1, 0, 2, 3]) == [2, 3]

def test_all_positive():
    assert filter_positive_numbers([1, 2, 3]) == [1, 2, 3]

def test_all_non_positive():
    assert filter_positive_numbers([-5, 0, -1]) == []

def test_empty():
    assert filter_positive_numbers([]) == []
