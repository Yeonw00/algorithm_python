"""
문제: 애너그램 그룹화

문자열 리스트 words가 주어질 때, 애너그램(철자만 다른 같은 구성의 단어)끼리 그룹지어 리스트로 묶어 반환하는 함수를 작성하세요.

예시:
입력: ["bat", "tab", "tap", "pat", "cat"]
출력: [["bat", "tab"], ["tap", "pat"], ["cat"]]

순서는 상관없음.

"""
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    return list(anagram_dict.values())