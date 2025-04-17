"""
문제: 과반수 요소 찾기

정수 리스트 numbers가 주어질 때, 전체 요소의 과반수 이상을 차지하는 요소를 반환하는 함수를 작성하세요.
항상 과반수 요소가 존재한다고 가정합니다.

예시:
입력: [3, 3, 4, 2, 3, 3, 3]
출력: 3

"""
from collections import Counter

def find_majority_element(numbers: list[int]) -> int:
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]

# find_majority_element([3, 3, 4, 2, 3, 3, 3])