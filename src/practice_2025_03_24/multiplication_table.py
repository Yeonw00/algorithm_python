# N단 구구단 출력
# 사용자로부터 숫자 N을 받아 N단 구구단을 출력하세요.

def multiplication_table(n:int):
    for i in range(1,10):
        print(f"{n} x {i} = {n * i}")