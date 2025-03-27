"""
문제: 중복 제거

정수 리스트 numbers가 주어질 때, 중복을 제거하고 정렬된 리스트를 반환하는 함수를 작성하세요.

"""
def unique_elements(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))

