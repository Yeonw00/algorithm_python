from src.practice_2025_03_24.find_min_max import find_min_max

def test_basic():
    assert find_min_max([3, 1, 4]) == (1, 4)

def test_single():
    assert find_min_max([5]) == (5, 5)

def test_empty():
    assert find_min_max([]) == (None, None)
