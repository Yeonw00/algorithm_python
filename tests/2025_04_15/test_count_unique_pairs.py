from src.practice_2025_04_15.count_unique_pairs import count_unique_pairs

def test_basic():
    assert count_unique_pairs([1, 3, 2, 2, 4], 4) == 2  # (1,3), (2,2)

def test_no_pair():
    assert count_unique_pairs([1, 2, 3], 10) == 0

def test_duplicates():
    assert count_unique_pairs([1, 1, 1, 1], 2) == 1  # only (1,1)
