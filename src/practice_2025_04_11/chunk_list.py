"""
문제: 리스트 분할

정수 리스트 numbers와 양의 정수 chunk_size가 주어질 때, 리스트를 chunk_size 길이만큼 나눈 2차원 리스트를 반환하는 함수를 작성하세요.
마지막 chunk는 길이가 chunk_size보다 작을 수 있습니다.

예시:
입력: [1, 2, 3, 4, 5], chunk_size = 2
출력: [[1, 2], [3, 4], [5]]

"""

# def chunk_list(numbers: list[int], chunk_size: int) -> list[list[int]]:
#       result = []
#       for i in range(0, len(numbers), chunk_size):
#             chunk = numbers[i:i+chunk_size]
#             result.append(chunk)
#       return result


def chunk_list(numbers: list[int], chunk_size: int) -> list[list[int]]:
    return [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]