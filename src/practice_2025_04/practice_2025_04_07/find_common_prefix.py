"""
문제: 공통 접두사 찾기

문자열 리스트 words가 주어졌을 때, 모든 문자열에 공통으로 포함되는 가장 긴 접두사를 찾아 반환하는 함수를 작성하세요.
공통 접두사가 없을 경우 빈 문자열을 반환합니다.

예시:
입력: ["flower", "flow", "flight"]
출력: "fl"

"""
def find_common_prefix(words: list[str]) -> str:
    if not words:
        return ""

    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix






