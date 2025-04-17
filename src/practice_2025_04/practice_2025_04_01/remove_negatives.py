"""
문제: 음수 제거

정수 리스트 numbers가 주어질 때, 음수 값을 제거한 리스트를 반환하는 함수를 작성하세요.

"""
def remove_negatives(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number >= 0]
