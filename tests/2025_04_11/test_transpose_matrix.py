from src.practice_2025_04_11.transpose_matrix import transpose_matrix

def test_basic():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_square_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_single_row():
    assert transpose_matrix([[1, 2, 3]]) == [[1], [2], [3]]

def test_single_column():
    assert transpose_matrix([[1], [2], [3]]) == [[1, 2, 3]]
