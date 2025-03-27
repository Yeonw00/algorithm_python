from src.practice_2025_03_27.sum_odd_numbers import sum_odd_numbers

def test_basic():
    assert sum_odd_numbers([1, 2, 3, 4, 5]) == 9

def test_no_odds():
    assert sum_odd_numbers([2, 4, 6]) == 0

def test_all_odds():
    assert sum_odd_numbers([1, 3, 5, 7]) == 16

def test_empty():
    assert sum_odd_numbers([]) == 0
