# 중복 문자를 제거한 문자열 생성
# 예: input -> "banana" → "ban"

# def remove_duplicate_chars(words:str, unique_chars=None) -> str :
#     if unique_chars is None:
#         unique_chars=[]
#
#     for index, word in enumerate(words) :
#         if word in unique_chars :
#             continue
#         unique_chars.append(word)
#
#     return ''.join(unique_chars)

def remove_duplicate_chars(words:str) -> str:
    seen = set()
    result = []
    for char in words:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)