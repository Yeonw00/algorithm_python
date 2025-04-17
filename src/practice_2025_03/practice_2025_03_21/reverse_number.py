#정수를 입력받아 숫자를 뒤집어 출력하는 프로그램을 작성하세요. (음수도 포함)

def reverse_integer(num):

    if num.startswith("-"):
        return -int(num[1::][::-1])

    else:
        return int(num[::-1])
