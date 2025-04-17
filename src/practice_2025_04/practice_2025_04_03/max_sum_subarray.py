"""
문제: 연속 부분 배열의 최대 합

정수 리스트 numbers가 주어질 때, 연속된 부분 배열(subarray) 중 합이 최대인 값을 반환하는 함수를 작성하세요.
(카데인 알고리즘 사용 가능)

예시:
입력: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
출력: 6  (부분 배열: [4, -1, 2, 1])

"""
def max_sum_subarray(numbers: list[int]) -> int:
    max_sum = curr_sum = numbers[0]
    for number in numbers[1:]:
        curr_sum = max(number, curr_sum + number)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# number = 1
# curr_sum = max(1, -1) = 1
# max_sum = max(-2, 1) = 1
# number = -3
# curr_sum = max(-3, -2) = -2
# max_sum = max(1, -2) = 1
# number = 4
# curr_sum = max(4, 2) = 4
# max_sum = max(1, 4) = 4
# number = -1
# curr_sum = max(-1, 3) = 3
# max_sum = max(4, 3) = 4
# number = 2
# curr_sum m= max(2, 5) = 5
# max_sum = max(4, 5) = 5
# number = 1
# curr_sum = max(1, 6) = 6
# max_sum = max(5, 6) = 6
# number = -5
# curr_sum = max(-5, 1) = 1
# max_sum = max(6, 1) = 6
# number = 4
# curr_sum = max(4, 5) = 5
# max_sum = max(6, 5) = 6

