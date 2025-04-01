"""
문제: 빈 문자열 제거

문자열 리스트 strings가 주어질 때, 빈 문자열("")을 제거한 새 리스트를 반환하는 함수를 작성하세요.

"""
def remove_empty_strings(strings: list[str]) -> list[str]:
    return [s for s in strings if s != ""]


