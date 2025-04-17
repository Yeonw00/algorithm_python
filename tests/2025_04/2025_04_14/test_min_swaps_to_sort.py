from src.practice_2025_04.practice_2025_04_14 import min_swaps_to_sort

def test_reversed():
    assert min_swaps_to_sort([4, 3, 2, 1]) == 2

def test_sorted():
    assert min_swaps_to_sort([1, 2, 3]) == 0

def test_random():
    assert min_swaps_to_sort([2, 3, 4, 1, 5]) == 3