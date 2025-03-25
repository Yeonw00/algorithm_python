from src.practice_2025_03_24.reverse_list import reverse_list

def test_basic():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

def test_single():
    assert reverse_list([1]) == [1]

def test_empty():
    assert reverse_list([]) == []
