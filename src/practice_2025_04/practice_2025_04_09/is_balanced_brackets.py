"""
문제: 괄호 균형 검사

문자열 s가 주어질 때, (), [], {} 괄호가 올바르게 짝지어졌는지 여부를 반환하는 함수를 작성하세요.

예시:
입력: "{[()]}" → 출력: True
입력: "([)]" → 출력: False

"""

def is_balanced_brackets(s: str) -> bool:
    bracket_dict = {")":"(", "}":"{", "]":"["}
    stack = []
    for c in s:
        if  c in bracket_dict.values():
            stack.append(c)
        elif c in bracket_dict.keys():
            if not stack or stack.pop() != bracket_dict[c]:
                return False
    return not stack