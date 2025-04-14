"""
문제: 정렬을 위한 최소 스왑 수

서로 다른 정수들로 구성된 리스트 arr가 주어질 때, 이를 오름차순으로 정렬하는 데 필요한 최소 스왑 횟수를 구하는 함수를 작성하세요.

예시:
입력: [4, 3, 2, 1]
출력: 2

"""

def min_swaps_to_sort(arr: list[int]) -> int:
    result = 0
    sorted_list = sorted(arr)
    idx =0
    while idx < len(arr):
        if arr == sorted_list:
            break
        min_num = min(arr[idx:])
        min_idx = arr.index(min_num)
        if min_idx == idx:
            idx += 1
        else:
            arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
            result += 1
            idx += 1

    return result




