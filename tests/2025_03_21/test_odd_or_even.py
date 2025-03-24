from src.practice_2025_03_21.odd_or_even import is_even

def test_even_numbers():
    assert is_even(2) == "짝수입니다"
    assert is_even(0) == "짝수입니다"
    assert is_even(100) == "짝수입니다"

def test_odd_numbers():
    assert is_even(1) == "홀수입니다"
    assert is_even(99) == "홀수입니다"
    assert is_even(-3) == "홀수입니다"