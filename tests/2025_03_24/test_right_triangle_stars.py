from io import StringIO
import sys
from src.practice_2005_03_24.right_triangle_stars import right_triangle_stars

def test_output(capsys):
    right_triangle_stars(3)
    captured = capsys.readouterr()
    assert captured.out == "*\n**\n***\n"
