from src.practice_2025_04.practice_2025_04_02.is_subsequence import is_subsequence

def test_true_case():
    assert is_subsequence("abc", "ahbgdc") is True

def test_false_case():
    assert is_subsequence("axc", "ahbgdc") is False

def test_empty_s():
    assert is_subsequence("", "anything") is True

def test_empty_t():
    assert is_subsequence("abc", "") is False
