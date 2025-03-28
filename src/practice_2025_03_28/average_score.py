"""
문제: 평균 점수 계산

학생들의 시험 점수가 리스트로 주어질 때, 평균을 계산하여 소수 첫째 자리까지 반올림하여 반환하는 함수를 작성하세요.
"""
def average_score(scores: list[int]) -> float:
    return round(sum(scores)/len(scores), 1) if scores else 0.0

# if not scores -> 'scores가 비어있다면'의 의미