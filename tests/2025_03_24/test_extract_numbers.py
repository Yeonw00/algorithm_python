import pytest
from src.practice_2025_03_24.extract_numbers import extract_numbers

def test_basic():
    assert extract_numbers("a1b2c3") == 123

def test_no_digits():
    with pytest.raises(ValueError):
        extract_numbers("abc")
