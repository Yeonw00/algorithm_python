"""
문제: 팰린드롬 판별

문자열 s가 주어졌을 때, 이 문자열이 앞에서 읽든 뒤에서 읽든 같은 문자열인지 여부를 판단하는 함수를 작성하세요.
대소문자는 구분하지 않으며, 공백은 무시합니다.

함수 시그니처:
def is_palindrome(s: str) -> bool:
    ...
"""

def is_palindrome(s: str) -> bool:
    if s==s[::-1]:
        return True
    else:
        return False
