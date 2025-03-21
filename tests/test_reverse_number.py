# test_reverse_number.py
from src.practice_2025_03_21.reverse_number import reverse_integer

def test_reverse_positive():
    assert reverse_integer("123") == 321
    assert reverse_integer("1000") == 1
    assert reverse_integer("10") == 1

def test_reverse_negative():
    assert reverse_integer("-456") == -654
    assert reverse_integer("-100") == -1
    assert reverse_integer("-1") == -1

def test_reverse_zero():
    assert reverse_integer("0") == 0
