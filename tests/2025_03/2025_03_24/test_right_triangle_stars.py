from src.practice_2025_03.practice_2025_03_24 import right_triangle_stars

def test_output(capsys):
    right_triangle_stars(3)
    captured = capsys.readouterr()
    assert captured.out == "*\n**\n***\n"
