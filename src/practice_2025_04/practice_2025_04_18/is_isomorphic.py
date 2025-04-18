"""
문제: 이형 사상 문자열

두 문자열 s와 t가 주어질 때, s의 각 문자를 t의 문자로 일대일 매핑하여 변환할 수 있다면 True를, 아니라면 False를 반환하세요.
(문자 간 매핑은 고정되어야 하며 중복 매핑은 허용되지 않음)

예시:
입력: s = "egg", t = "add" → 출력: True
입력: s = "foo", t = "bar" → 출력: False

"""
# def is_isomorphic(s: str, t: str) -> bool:
#     d = dict()
#     new_word = ''
#     if len(set(s)) != len(set(t)):
#         return False
#     for i in range(len(s)):
#         d[s[i]] = t[i]
#     for i in s:
#         i = d[i]
#         new_word += i
#
#     if new_word == t:
#         return True
#     else:
#         return False

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # 이중 매핑을 통해 **일대일 대응**을 보장
    s_to_t = {}
    t_to_s = {}

    for sc, tc in zip(s, t):
        # 이미 매핑된 적이 있는데 다른 문자로 다시 매핑하려 한다면
        if (sc in s_to_t and s_to_t[sc] != tc) or (tc in t_to_s and t_to_s[tc] != sc):
            return False
        s_to_t[sc] = tc
        t_to_s[tc] = sc

    return True