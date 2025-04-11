from src.practice_2025_04_11.chunk_list import chunk_list

def test_even_chunks():
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

def test_uneven_chunks():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_chunk_size_larger_than_list():
    assert chunk_list([1, 2], 5) == [[1, 2]]

def test_empty_list():
    assert chunk_list([], 3) == []
