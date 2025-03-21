#정수를 입력받아 숫자를 뒤집어 출력하는 프로그램을 작성하세요. (음수도 포함)

num=input("정수를 입력해주세요 : ")

if num.startswith("-"):
    reversed_num = int(num[1::][::-1])
    print(-reversed_num)
else:
    reversed_num = int(num[::-1])
    print(reversed_num)