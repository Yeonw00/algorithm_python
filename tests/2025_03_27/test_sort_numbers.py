from src.practice_2025_03_27.sort_numbers import sort_numbers

def test_case_1():
    assert sort_numbers([4, 2, 9, 1, 7]) == "1 2 4 7 9"

def test_case_2():
    assert sort_numbers([10, 5, 3]) == "3 5 10"

def test_min_limit():
    assert sort_numbers([1]) == "1"

def test_max_limit():
    assert sort_numbers(list(range(100, 0, -1))) == " ".join(str(i) for i in range(1, 101))

def test_invalid_length():
    try:
        sort_numbers([])
        assert False  # 여기에 도달하면 실패
    except ValueError:
        assert True
