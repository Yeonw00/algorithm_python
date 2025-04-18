# 정수가 소수인지 판별하는 함수
# 숫자 N이 소수인지 판별하는 함수를 작성하세요.

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5)+1, 2):
            if n % i ==0:
                return False
        return True

