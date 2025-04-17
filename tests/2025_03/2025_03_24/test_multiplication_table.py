from src.practice_2025_03.practice_2025_03_24 import multiplication_table

def test_output(capsys):
    multiplication_table(2)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert lines[0] == "2 x 1 = 2"
    assert lines[-1] == "2 x 9 = 18"
