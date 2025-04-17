from src.practice_2025_03.practice_2025_03_21 import reverse_negative_string

def test_reverse_negative():
    assert reverse_negative_string("-123") == "-321"
    assert reverse_negative_string("-100") == "-001"
    assert reverse_negative_string("-1") == "-1"

def test_reverse_positive():
    assert reverse_negative_string("456") == "음수 부호가 포함되지 않았습니다."
    assert reverse_negative_string("0") == "음수 부호가 포함되지 않았습니다."

def test_reverse_invalid_input():
    assert reverse_negative_string("") == "음수 부호가 포함되지 않았습니다."
    assert reverse_negative_string("-") == "-"
