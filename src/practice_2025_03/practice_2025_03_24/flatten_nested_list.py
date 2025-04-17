# 중첩 리스트 평탄화
# 예: input -> [1, [2, [3]]] → [1, 2, 3]

def flatten_nested_list(lists:list) -> list:
    result = []
    for item in lists:
        if isinstance(item, list):  # 안에 또 리스트면 재귀 호출
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)

    return result