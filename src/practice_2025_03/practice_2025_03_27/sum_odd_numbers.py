"""
문제: 홀수 합 구하기

정수 리스트 numbers가 주어질 때, 그 안에 포함된 홀수들의 합을 반환하는 함수를 작성하세요.

"""
def sum_odd_numbers(numbers: list[int]) -> int:
    return sum(number for number in numbers if number % 2 !=0)