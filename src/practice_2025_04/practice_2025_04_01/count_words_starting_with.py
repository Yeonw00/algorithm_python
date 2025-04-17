"""
문제: 특정 문자로 시작하는 단어 개수 세기

문자열 sentence와 문자 char가 주어질 때, 해당 문자를 첫 글자로 갖는 단어의 개수를 반환하는 함수를 작성하세요.
대소문자는 구분하지 않습니다.

"""
def count_words_starting_with(sentence: str, char: str) -> int:
    return sum(1 for c in sentence.split() if c.lower().startswith(char.lower()))