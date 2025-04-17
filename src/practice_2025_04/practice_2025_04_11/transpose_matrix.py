"""
문제: 행렬 전치

2차원 정수 리스트 matrix가 주어질 때, 이를 전치(transpose)한 행렬을 반환하는 함수를 작성하세요.

예시:
입력: [[1, 2, 3], [4, 5, 6]]
출력: [[1, 4], [2, 5], [3, 6]]

"""
def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]

# def transpose(matrix: list[list[int]]) -> list[list[int]]:
#     rows = len(matrix)
#     cols = len(matrix[0])
#     result = []
#
#     for col in range(cols):
#         new_row = []
#         for row in range(rows):
#             new_row.append(matrix[row][col])
#         result.append(new_row)
#
#     return result