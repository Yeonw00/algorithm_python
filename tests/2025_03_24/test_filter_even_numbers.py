from src.practice_2025_03_24.filter_even_numbers import filter_even_numbers

def test_mixed():
    assert filter_even_numbers([1, 2, 3, 4]) == [2, 4]

def test_all_even():
    assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]

def test_all_odd():
    assert filter_even_numbers([1, 3, 5]) == []

def test_empty():
    assert filter_even_numbers([]) == []
