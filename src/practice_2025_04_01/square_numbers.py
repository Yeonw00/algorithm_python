"""
문제: 제곱 리스트 만들기

정수 리스트 numbers가 주어질 때, 각 요소의 제곱으로 구성된 새로운 리스트를 반환하는 함수를 작성하세요.

"""
# def square_numbers(numbers: list[int]) -> list[int]:
#     new_list = []
#     result = 0
#     for number in numbers:
#         result = number * number
#         new_list.append(result)
#     return new_list


def square_numbers(numbers: list[int]) -> list[int]:
    return [number * number for number in numbers]