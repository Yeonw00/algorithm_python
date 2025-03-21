#사용자로부터 문자열을 입력받아, 단어의 순서를 거꾸로 출력하는 프로그램을 작성하세요.

# 공백 상관 없이 문자열을 거꾸로 출력할 때
# words = input("문자열을 입력하세요: ")
# print(words[::-1])


# sentence = input("문장을 입력하세요: ")
# words = sentence.split()
# reversed_sentence = " ".join(reversed(words))
# print(reversed_sentence)

def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])
