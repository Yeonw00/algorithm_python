from src.practice_2025_04.practice_2025_04_10 import second_largest

def test_basic():
    assert second_largest([1, 3, 2]) == 2

def test_with_duplicates():
    assert second_largest([4, 4, 3, 2]) == 3

def test_negative_numbers():
    assert second_largest([-10, -20, -5]) == -10

def test_large_input():
    assert second_largest(list(range(1000))) == 998
