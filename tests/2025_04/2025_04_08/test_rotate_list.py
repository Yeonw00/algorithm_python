from src.practice_2025_04.practice_2025_04_08.rotate_list import rotate_list

def test_basic():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_more_than_length():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]

def test_rotate_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_empty():
    assert rotate_list([], 3) == []


