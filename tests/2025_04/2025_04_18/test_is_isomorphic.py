from src.practice_2025_04.practice_2025_04_18.is_isomorphic import is_isomorphic

def test_true_cases():
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("paper", "title") is True

def test_false_cases():
    assert is_isomorphic("foo", "bar") is False
    assert is_isomorphic("ab", "aa") is False
