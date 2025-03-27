# 문제: 짝수 인덱스 문자열
# 문자열이 주어졌을 때, 짝수 인덱스에 해당하는 문자들만 이어서 출력하는 프로그램을 작성하시오.

def even_index_chars(words:str) -> str:
    return words[::2]
