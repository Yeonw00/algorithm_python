#문자열의 특정 구간만 선택해서 거꾸로 뒤집어 출력하세요.
#(힌트: 슬라이싱 범위를 지정해보세요)

def reverse_partial_string(words:str, start:int, end:int) -> str :
    if not (0 <= start <= end <= len(words)):
        raise ValueError("올바른 인덱스 범위가 아닙니다.")
    return words[:start] + words[start:end][::-1] + words[end:]