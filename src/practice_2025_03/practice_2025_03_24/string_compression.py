# 반복 문자 압축하기
# 예: input -> "aaabbc" → "a3b2c1"
from collections import Counter

# def string_compression(words:str) -> str:
#     char_list = Counter(words)
#     result = ""
#     for i in char_list:
#         result += i+str(char_list[i])
#     return result

def string_compression(words: str) -> str:
    counts = Counter(words)
    return ''.join(f"{char}{count}" for char, count in counts.items())