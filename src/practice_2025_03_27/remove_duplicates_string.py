"""
문제: 중복 문자 제거

문자열 s가 주어질 때, 문자열 내에서 중복된 문자를 제거하고 순서를 유지한 새로운 문자열을 반환하는 함수를 작성하세요.

예시: "banana" → "ban"

"""
def remove_duplicates_string(s: str) -> str:
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)