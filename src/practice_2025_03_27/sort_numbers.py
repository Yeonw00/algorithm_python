# 문제: 숫자 정렬기

# 사용자로부터 정수 N개를 입력받아 오름차순으로 정렬한 결과를 출력하는 프로그램을 작성하시오.

def sort_numbers(numbers: list[int]) -> str:
    n = len(numbers)
    if n < 1 or n > 100:
        raise ValueError("입력값은 1 이상 100 이하이어야 합니다.")
    sorted_numbers = sorted(numbers)
    return " ".join(map(str, sorted_numbers))


