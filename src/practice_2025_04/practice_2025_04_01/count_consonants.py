"""
문제: 자음 개수 세기

영문 문자열 s가 주어질 때, 그 안에 포함된 자음의 개수를 반환하는 함수를 작성하세요.
모음(a, e, i, o, u)을 제외한 알파벳이 자음입니다. 대소문자는 구분하지 않습니다.

"""
def count_consonants(s: str) -> int:
    s =  s.lower()
    count = 0
    for c in s:
        if c.isalpha() and c not in "aeiou":
            count += 1
    return count

