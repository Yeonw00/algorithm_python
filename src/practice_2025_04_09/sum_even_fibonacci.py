"""
문제: 짝수 피보나치 수의 합

정수 n이 주어질 때, n 이하의 피보나치 수 중 짝수들의 합을 구하는 함수를 작성하세요.

예시:
입력: 10
피보나치 수: 1, 1, 2, 3, 5, 8 → 짝수는 2, 8 → 합은 10
"""
def sum_even_fibonacci(n: int) -> int:
    a, b = 0, 1  # 초기 피보나치 숫자
    total = 0

    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b  # 피보나치 갱신

    return total
