"""
문제: 가장 긴 고유 문자 부분 문자열

문자열 s가 주어졌을 때, 중복되지 않는 문자가 연속으로 이어진 가장 긴 부분 문자열의 길이를 반환하는 함수를 작성하세요.

예시:
입력: "abcabcbb"
출력: 3  (부분 문자열 "abc")

"""
# def longest_unique_substring(s: str) -> int:
#     if len(s) == 0:
#         return 0
#     idx = 0
#     result = s[0]
#     max_sum = 1
#     curr_sum = 1
#     for c in s[1:]:
#         if c not in result:
#             result += c
#             curr_sum = max(curr_sum, curr_sum + 1)
#             max_sum = max(max_sum, curr_sum)
#         else:
#             result = c
#             curr_sum = 1
#     return max_sum


def longest_unique_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


