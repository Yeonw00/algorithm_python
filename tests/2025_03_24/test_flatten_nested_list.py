from src.practice_2025_03_24.flatten_nested_list import flatten

def test_nested():
    assert flatten([1, [2, [3]]]) == [1, 2, 3]

def test_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]

def test_empty():
    assert flatten([]) == []
