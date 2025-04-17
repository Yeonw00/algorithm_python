"""
문제: 리스트 요소 곱하기

정수 리스트 numbers가 주어질 때, 모든 요소의 곱을 반환하는 함수를 작성하세요.

"""
def multiply_elements(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result
