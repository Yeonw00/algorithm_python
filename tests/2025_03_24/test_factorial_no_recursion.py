from src.practice_2025_03_24.factorial_no_recursion import factorial_no_recursion

def test_basic():
    assert factorial_no_recursion(5) == 120

def test_zero():
    assert factorial_no_recursion(0) == 1
