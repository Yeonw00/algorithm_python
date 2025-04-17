"""
문제: 두 번째로 큰 수 찾기

정수 리스트 numbers가 주어질 때, 그 중 두 번째로 큰 수를 반환하는 함수를 작성하세요.
리스트에는 최소 두 개의 서로 다른 수가 포함되어 있다고 가정합니다.

"""

# 전체 정렬하는 방법 -> 비효율적 O(n log n)
# def second_largest(numbers: list[int]) -> int:
#     s = sorted(set(numbers), reverse=True)
#     return s[1]

# 큰 수 두개만 찾는 방법 -> 효율적 O(n)

#float('-inf') -> 음의 무한대 -> 가장 작은 수라는 의미

def second_largest(numbers: list[int]) -> int:
    first = second = float('-inf')

    for num in numbers:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second