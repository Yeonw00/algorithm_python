"""
문제: 리스트 회전

정수 리스트 numbers와 정수 k가 주어질 때, 리스트를 오른쪽으로 k만큼 회전시킨 결과를 반환하는 함수를 작성하세요.

예시:
입력: [1, 2, 3, 4, 5], k = 2
출력: [4, 5, 1, 2, 3]

"""

def rotate_list(numbers: list[int], k: int) -> list[int]:
    if not numbers:
        return []
    k %= len(numbers)
    return numbers[-k:] + numbers[:-k]

