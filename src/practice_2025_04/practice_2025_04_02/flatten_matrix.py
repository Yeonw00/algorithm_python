"""
문제: 2차원 리스트 평탄화

정수로 이루어진 2차원 리스트(matrix)가 주어질 때, 모든 요소를 하나의 1차원 리스트로 평탄화하여 반환하는 함수를 작성하세요.

예시:
입력: [[1, 2], [3, 4], [5]]
출력: [1, 2, 3, 4, 5]

"""

def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    new_list = []
    for i in matrix:
        new_list.extend(i)
    return new_list

# 리스트 컴프리헨션
# def flatten_matrix(matrix: list[list[int]]) -> list[int]:
#     return [item for row in matrix for item in row]
# 아래의 코드와 같음
# result = []
# for row in matrix:
#     for item in row:
#         result.append(item)
# return result

