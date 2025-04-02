from src.practice_2025_04_02.merge_and_sort_lists import merge_and_sort_lists

def test_basic_merge():
    assert merge_and_sort_lists([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert merge_and_sort_lists([1, 1, 2], [2, 2, 3]) == [1, 2, 3]

def test_empty_one_list():
    assert merge_and_sort_lists([], [4, 1, 2]) == [1, 2, 4]

def test_both_empty():
    assert merge_and_sort_lists([], []) == []
