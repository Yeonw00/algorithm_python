from src.practice_2025_03_27.unique_elements import unique_elements

def test_with_duplicates():
    assert unique_elements([3, 1, 2, 3, 2, 1]) == [1, 2, 3]

def test_no_duplicates():
    assert unique_elements([5, 3, 8]) == [3, 5, 8]

def test_sorted_input():
    assert unique_elements([1, 2, 3]) == [1, 2, 3]

def test_empty_list():
    assert unique_elements([]) == []
