"""
문제: 리스트 병합 및 정렬

두 개의 정수 리스트 list1, list2가 주어질 때, 이들을 병합하고 중복을 제거한 뒤 오름차순으로 정렬하여 반환하는 함수를 작성하세요.

"""
def merge_and_sort_lists(list1: list[int], list2: list[int]) -> list[int]:
    list1.extend(list2)
    return sorted(set(list1))
