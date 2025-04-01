from src.practice_2025_04_01.square_numbers import square_numbers

def test_basic():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]

def test_negative():
    assert square_numbers([-1, -2, 0]) == [1, 4, 0]

def test_empty():
    assert square_numbers([]) == []
