"""
문제: 가장 많이 등장한 요소

정수 리스트 numbers가 주어질 때, 가장 많이 등장한 정수를 반환하는 함수를 작성하세요.
여러 개일 경우 먼저 등장한 요소를 반환합니다.

"""
from collections import Counter
def most_frequent_element(numbers: list[int]) -> int:
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]
