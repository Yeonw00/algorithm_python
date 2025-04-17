from src.practice_2025_04.practice_2025_04_01.remove_negatives import remove_negatives

def test_basic():
    assert remove_negatives([1, -2, 3, -4]) == [1, 3]

def test_all_negative():
    assert remove_negatives([-1, -2, -3]) == []

def test_all_positive():
    assert remove_negatives([5, 10, 2]) == [5, 10, 2]

def test_empty():
    assert remove_negatives([]) == []
