from src.practice_2025_03_28.average_score import average_score

def test_basic():
    assert average_score([80, 90, 100]) == 90.0

def test_rounding():
    assert average_score([90, 91]) == 90.5

def test_all_same():
    assert average_score([75, 75, 75]) == 75.0

def test_empty():
    assert average_score([]) == 0.0
