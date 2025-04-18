from src.practice_2025_04.practice_2025_04_18.maximum_product_subarray import maximum_product_subarray

def test_basic():
    assert maximum_product_subarray([2, 3, -2, 4]) == 6

def test_negative_only():
    assert maximum_product_subarray([-2, -3, -4]) == 12

def test_mix():
    assert maximum_product_subarray([-2, 0, -1]) == 0

def test_single():
    assert maximum_product_subarray([5]) == 5
