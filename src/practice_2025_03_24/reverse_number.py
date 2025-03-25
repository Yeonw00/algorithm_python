# 정수 N이 주어졌을 때 그 숫자를 거꾸로 뒤집어 반환하세요.
# 예: input -> 1234 → 4321

def reverse_number(number: int) -> int:
    return int(str(number)[::-1])