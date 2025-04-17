"""
문제: 고유한 합을 만드는 쌍의 개수

정수 리스트 numbers와 정수 target이 주어질 때, 합이 target이 되는 고유한 (a, b) 쌍의 개수를 반환하세요.
(순서와 중복은 무시, a < b 인 경우만 계산)

예시:
입력: numbers = [1, 3, 2, 2, 4], target = 4
출력: 2  → (1,3), (2,2)

함수 시그니처:
    ...
"""
# def count_unique_pairs(numbers: list[int], target: int) -> int:
#     idx = 0
#     l = len(numbers)
#     t = []
#     while idx < l-1:
#         n = numbers[idx]
#         for num in numbers[idx+1:]:
#             if n <= num and n + num == target:
#                 t.append((n, num))
#         idx += 1
#     return len(set(t))

def count_unique_pairs(numbers: list[int], target: int) -> int:
    # 지금까지 등장한 숫자들을 저장하는 집합
    seen = set()
    # **유일한 쌍**만 저장하기 위한 집합
    pairs = set()

    for num in numbers:
        # 현재 숫자 `num`과 더해서 `target`이 되기 위한 숫자(보완값)를 구함
        complement = target - num
        if complement in seen:
            # (num, complement)`를 튜플로 만들되, **정렬**해서 순서를 통일
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    return len(pairs)
