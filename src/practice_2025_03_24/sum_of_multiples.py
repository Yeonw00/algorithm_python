# 1~100 중 3 또는 5의 배수 합 구하기

def sum_of_multiples() -> int:
    result = 0
    for x in range(1,101):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result


