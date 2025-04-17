#음수 부호가 포함된 문자열을 입력받아, 숫자 부분만 뒤집어 출력되도록 처리하세요.
#(예: -987 → -789)

def reverse_negative_string(num:str) -> str :
    if num.startswith("-"):
        return "-"+num[1::][::-1]
    else:
        return "음수 부호가 포함되지 않았습니다."
