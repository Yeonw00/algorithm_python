"""
문제: 각 단어의 첫 글자 대문자 만들기

문자열 s가 주어질 때, 각 단어의 첫 글자만 대문자로 바꾸고 나머지는 소문자로 바꾼 문자열을 반환하는 함수를 작성하세요.

예시: "hello world" → "Hello World"

"""
def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())