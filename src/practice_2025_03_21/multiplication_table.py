#사용자로부터 2~9 사이의 숫자를 입력받아 해당 숫자의 구구단을 출력하는 프로그램을 작성하세요.

# num = int(input("2~9 사이의 숫자를 입력하세요 : "))
# if 2<=num<=9:
#     for a in range(1,10):
#         print(f"{num} * {a} = {num * a}")
# else:
#     print("2~9 사이의 숫자만 입력해주세요.")

def generate_multiplication_table(n: int) -> list[str]:
    if not 2 <= n <= 9:
        raise ValueError("2에서 9 사이의 숫자만 입력해주세요.")
    return [f"{n} x {i} = {n * i}" for i in range(1, 10)]
