#숫자로 이루어진 리스트가 주어질 때, 리스트의 평균을 구하는 프로그램을 작성하세요.

# 리스트를 입력받을 때
#a = [int(x) for x in input().split()]

a = [10, 20, 30, 40, 50]
avg = sum(a) / len(a)
print(f"평균은 {avg}입니다.")