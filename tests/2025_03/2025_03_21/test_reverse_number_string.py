from src.practice_2025_03.practice_2025_03_21.reverse_number_string import reverse_number_string

def test_reverse_simple_numbers():
    assert reverse_number_string("12345") == "54321"
    assert reverse_number_string("1000") == "0001"

def test_reverse_with_leading_zeros():
    assert reverse_number_string("00123") == "32100"

def test_reverse_empty():
    assert reverse_number_string("") == ""

def test_reverse_single_digit():
    assert reverse_number_string("7") == "7"