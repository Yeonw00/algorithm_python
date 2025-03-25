# 재귀 없이 팩토리얼 함수 구현
# 정수 N을 입력받아 팩토리얼 값을 반환하는 함수를 작성하세요.

def factorial_no_recursion(n:int) -> int:
    result = 1
    for i in range(2,n+1):
        result *= i
    return result
