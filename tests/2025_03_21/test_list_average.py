from src.practice_2025_03_21.list_average import calculate_average

def test_average_basic():
    assert calculate_average([10, 20, 30]) == 20.0

def test_average_empty():
    assert calculate_average([]) == 0.0

def test_average_single():
    assert calculate_average([100]) == 100.0