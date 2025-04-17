from src.practice_2025_04.practice_2025_04_09 import sum_even_fibonacci

def test_basic():
    assert sum_even_fibonacci(10) == 10

def test_larger_limit():
    assert sum_even_fibonacci(34) == 44

def test_small():
    assert sum_even_fibonacci(1) == 0

def test_zero():
    assert sum_even_fibonacci(0) == 0
