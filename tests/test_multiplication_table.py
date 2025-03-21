from src.practice_2025_03_21.multiplication_table import generate_multiplication_table

def test_table_for_3():
    result = generate_multiplication_table(3)
    assert result[0] == "3 x 1 = 3"
    assert result[-1] == "3 x 9 = 27"
    assert len(result) == 9

def test_table_invalid_low():
    try:
        generate_multiplication_table(1)
        assert False  # 여기 도달하면 실패
    except ValueError:
        assert True

def test_table_invalid_high():
    try:
        generate_multiplication_table(10)
        assert False
    except ValueError:
        assert True