#정수를 입력받아 홀수인지 짝수인지 판별하는 프로그램을 작성하세요.

def is_even(num: int) -> str:
    if num % 2 == 0:
        return "짝수입니다"
    else:
        return "홀수입니다"