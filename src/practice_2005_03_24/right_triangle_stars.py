# 오른쪽 삼각형 별찍기
# 사용자로부터 숫자 N을 입력받아 다음과 같은 출력을 만드세요:
# (N이 4일 때)
# *
# **
# ***
# ****

def right_triangle_stars(n:int):
    for x in range(1,n+1):
        print("*" * x)

# def left_triangle_stars():
#     n = int(input())
#     for x in range(1, n+1):
#         print(" " * (n-x) + "*" * x)
