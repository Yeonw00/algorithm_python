from src.practice_2025_04.practice_2025_04_01 import group_anagrams

def test_grouping():
    words = ["bat", "tab", "tap", "pat", "cat"]
    result = group_anagrams(words)
    expected = [["bat", "tab"], ["tap", "pat"], ["cat"]]
    assert sorted([sorted(g) for g in result]) == sorted(sorted(g) for g in expected)

def test_empty():
    assert group_anagrams([]) == []

def test_single():
    assert group_anagrams(["abc"]) == [["abc"]]
