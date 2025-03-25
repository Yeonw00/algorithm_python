# 문자열이 회문인지 확인하는 함수 작성
# 예: input -> "level" → True, input -> "hello" → False

def palindrome_check(words:str) -> bool :
    return words == words[::-1]


