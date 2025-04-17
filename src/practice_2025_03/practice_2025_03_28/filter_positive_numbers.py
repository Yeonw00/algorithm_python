"""
문제: 양수 필터링

정수 리스트 numbers가 주어질 때, 그 중 0보다 큰 수만 추출하여 리스트로 반환하는 함수를 작성하세요.

"""
def filter_positive_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number > 0]

