from src.practice_2025_03.practice_2025_03_24 import reverse_number

def test_basic():
    assert reverse_number(1234) == 4321

def test_with_zero():
    assert reverse_number(100) == 1
