#문자열을 뒤집되, 각 글자 사이에 공백을 넣어서 출력하세요.
#(예: hello → o l l e h)

def reverse_with_spacing(words: str) -> str :
    return " ".join(words[::-1])