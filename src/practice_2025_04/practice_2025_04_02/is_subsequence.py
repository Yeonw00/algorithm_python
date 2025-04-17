"""
문제: 부분 수열인지 확인하기

문자열 s와 t가 주어질 때, s가 t의 부분 수열(subsequence)인지 여부를 반환하는 함수를 작성하세요.
부분 수열이란 문자의 순서를 유지한 채 일부만 포함되는 문자열입니다.

예시:
입력: s = "abc", t = "ahbgdc"
출력: True

"""
def is_subsequence(s: str, t: str) -> bool:
    s_idx, t_idx = 0, 0
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] == t[t_idx]:
            s_idx += 1
        t_idx += 1
    return s_idx == len(s)