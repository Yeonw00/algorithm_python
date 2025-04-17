from src.practice_2025_04.practice_2025_04_17.longest_consecutive_sequence import longest_consecutive_sequence

def test_basic():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4

def test_unsorted():
    assert longest_consecutive_sequence([0, -1, 1, 2, 4]) == 4

def test_single():
    assert longest_consecutive_sequence([10]) == 1

def test_empty():
    assert longest_consecutive_sequence([]) == 0
