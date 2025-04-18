"""
문제: 부분 배열의 최대 곱

정수 리스트 numbers가 주어질 때, 연속된 부분 배열 중 곱이 최대가 되는 값을 반환하는 함수를 작성하세요.

예시:
입력: [2, -5, -2, -4, 3]
출력: 24  (부분 배열: [-2, -4, 3])

"""
# def maximum_product_subarray(numbers: list[int]) -> int:
#     max_result = float('-inf')
#     if len(numbers) == 1:
#         max_result = numbers[0]
#     idx = 0
#     while idx < len(numbers)-1:
#         if idx == 0:
#             max_result = numbers[idx] * numbers[idx+1]
#             idx += 1
#             continue
#         if max_result * numbers[idx+1] < 0:
#             max_result = max(max_result, numbers[idx] * numbers[idx+1])
#         else:
#             max_result = max(max_result, max_result * numbers[idx])
#         idx +=1
#
#     return max_result

def maximum_product_subarray(numbers: list[int]) -> int:
    if not numbers:
        return 0

    max_prod = min_prod = result = numbers[0]

    for num in numbers[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result