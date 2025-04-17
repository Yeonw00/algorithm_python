"""
문제: 가장 긴 연속된 수열

정수 리스트 numbers가 주어질 때, 정렬하지 않고도 가장 긴 연속된 수열의 길이를 반환하는 함수를 작성하세요.

예시:
입력: [100, 4, 200, 1, 3, 2]
출력: 4  (1, 2, 3, 4)

"""
# def longest_consecutive_sequence(numbers: list[int]) -> int:
#     if not numbers:
#         return 0
#
#     sorted_numbers = sorted(set(numbers))
#     max_len = 1
#     current_len = 1
#
#     for i in range(1, len(sorted_numbers)):
#         if sorted_numbers[i] == sorted_numbers[i - 1] + 1:
#             current_len += 1
#             max_len = max(max_len, current_len)
#         else:
#             current_len = 1
#
#     return max_len

def longest_consecutive_sequence(numbers: list[int]) -> int:
    if not numbers:
        return 0

    # 리스트를 `set`으로 변환 → 중복 제거 + O(1) 탐색 가능
    num_set = set(numbers)
    max_len = 0

    for num in num_set:
        # 연속 시작점일 때만
        if num - 1 not in num_set:
            current = num
            # `streak`는 지금 연속된 숫자 구간의 길이 (초기 1)
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            max_len = max(max_len, streak)

    return max_len
