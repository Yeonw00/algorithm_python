from src.practice_2025_04.practice_2025_04_02 import flatten_matrix

def test_basic():
    matrix = [[1, 2], [3, 4], [5]]
    assert flatten_matrix(matrix) == [1, 2, 3, 4, 5]

def test_empty_inner():
    assert flatten_matrix([[1], [], [2, 3]]) == [1, 2, 3]

def test_empty_matrix():
    assert flatten_matrix([]) == []

def test_all_empty():
    assert flatten_matrix([[], [], []]) == []
