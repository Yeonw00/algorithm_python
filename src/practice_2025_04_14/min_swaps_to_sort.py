"""
문제: 정렬을 위한 최소 스왑 수

서로 다른 정수들로 구성된 리스트 arr가 주어질 때, 이를 오름차순으로 정렬하는 데 필요한 최소 스왑 횟수를 구하는 함수를 작성하세요.

예시:
입력: [4, 3, 2, 1]
출력: 2

"""

# def min_swaps_to_sort(arr: list[int]) -> int:
#     result = 0
#     sorted_list = sorted(arr)
#     idx =0
#     while idx < len(arr):
#         if arr == sorted_list:
#             break
#         min_num = min(arr[idx:])
#         min_idx = arr.index(min_num)
#         if min_idx == idx:
#             idx += 1
#         else:
#             arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
#             result += 1
#             idx += 1
#
#     return result

# 사이클 기반 최소 스왑 알고리즘
def min_swaps_to_sort(arr: list[int]) -> int:
    n = len(arr)
    """
    - 각 원소의 `(값, 원래 인덱스)`를 튜플로 저장한 리스트를 만들고
    - 그걸 **값 기준으로 정렬**
    → 정렬된 상태에서 각 값이 **원래 어디 있었는지를 기억**하는 구조 
    """
    arr_pos = sorted([(val, idx) for idx, val in enumerate(arr)])
    """
    방문 여부를 저장하는 리스트
    이미 사이클에 포함된 인덱스를 다시 처리하지 않기 위해 사용
    n=4 일때 visited = [False, False, False, False]
    """
    visited = [False] * n
    swaps = 0

    for i in range(n):
        """
        - 이미 방문한 인덱스인가?
        - 정렬 후 위치가 원래 위치와 같은가? → 스왑 필요 없음
        """
        if visited[i] or arr_pos[i][1] == i:
            continue

        # 현재 사이클의 길이
        cycle_len = 0
        # 현재 순회 중인 인덱스 (변수 이름만 바뀐 것)
        j = i

        while not visited[j]:
            # 현재 위치를 방문 처리해서 다시 안 오도록 함
            visited[j] = True
            # 현재 인덱스의 값이 **정렬된 배열 기준으로** 어디로 가야 하는지 확인하고 이동
            j = arr_pos[j][1]
            # 사이클 안에서 이동할 때마다 길이 +1
            cycle_len += 1

        swaps += cycle_len - 1

    return swaps




