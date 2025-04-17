from src.practice_2025_04.practice_2025_04_03 import max_sum_subarray

def test_example():
    assert max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_negative():
    assert max_sum_subarray([-5, -1, -8]) == -1

def test_all_positive():
    assert max_sum_subarray([1, 2, 3]) == 6

def test_single_element():
    assert max_sum_subarray([7]) == 7
