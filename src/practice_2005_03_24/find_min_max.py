# 최대값과 최소값 찾기 (함수 없이)
# 리스트에서 내장 함수 없이 최대값과 최소값을 구하세요.

def find_min_max(numbers:list) :
    if not numbers:
        return None, None

    min_num = max_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num,max_num