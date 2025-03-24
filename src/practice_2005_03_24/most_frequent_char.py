# 문자열에서 가장 자주 등장한 문자 찾기
# 예: input -> "hello" → "l"
from collections import Counter

def most_frequent_char(words:str) -> str :
    counter = Counter(words)
    return counter.most_common(1)[0][0]
