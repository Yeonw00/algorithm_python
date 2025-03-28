"""
문제: 가장 긴 단어 찾기

문자열 sentence가 주어질 때, 공백으로 구분된 단어들 중 가장 길이가 긴 단어를 반환하는 함수를 작성하세요.
여러 개일 경우 먼저 등장한 단어를 반환합니다.

"""
# def find_longest_word(sentence: str) -> str:
#     sentence_list = sentence.split()
#     longest_word = ""
#     for i in sentence_list:
#         if len(i)> len(longest_word):
#             longest_word = i
#     return longest_word

def find_longest_word(sentence: str) -> str:
    return max(sentence.split(), key=len, default="")
