"""
문제: 모음 개수 세기

영문 문자열 s가 주어질 때, 그 안에 포함된 모음(a, e, i, o, u)의 개수를 반환하는 함수를 작성하세요.
대소문자는 구분하지 않습니다.

"""
def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")