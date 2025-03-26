# 문자열에서 숫자만 추출하여 정수로 만들기
# 예: input -> "a1b2c3" → 123

def extract_numbers(words:str):
    char_list = list(words)
    new_word = ""
    for i in char_list:
        if i.isnumeric():
            new_word += i

    return int(new_word)


# def extract_numbers(words: str) -> int:
#     return int(''.join(filter(str.isdigit, words)))
