from src.practice_2025_03.practice_2025_03_27.multiply_elements import multiply_elements

def test_basic():
    assert multiply_elements([2, 3, 4]) == 24

def test_contains_zero():
    assert multiply_elements([1, 0, 5]) == 0

def test_one_element():
    assert multiply_elements([7]) == 7

def test_empty_list():
    assert multiply_elements([]) == 1  # 곱셈 항등원
