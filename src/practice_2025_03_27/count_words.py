# 문제: 단어 개수 세기

# 주어진 문장에서 단어의 개수를 세는 프로그램을 작성하시오.

def count_words(words:str) -> int:
    return len(words.split())

