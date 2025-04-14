"""
문제: IP 주소 유효성 검사

문자열 ip가 주어질 때, IPv4 형식이 올바른지 검사하여 True 또는 False를 반환하는 함수를 작성하세요.
IPv4는 0~255 범위의 숫자 4개가 점(.)으로 구분되어야 하며, 각 숫자는 불필요한 0으로 시작하지 않아야 합니다.

예시:
입력: "192.168.0.1" → 출력: True
입력: "256.100.50.0" → 출력: False

"""

# def validate_ip_address(ip: str) -> bool:
#     num_list = ip.split(".")
#     if len(num_list) != 4:
#         return False
#     for num in num_list:
#         if num.startswith('0'):
#             if len(num) > 1:
#                 return False
#         try:
#             n = int(num)
#         except ValueError:
#             return False
#         if 0<=n<=255:
#             continue
#         else:
#             return False
#     return True

def validate_ip_address(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part.startswith('0'):
            return False
        if not 0<=int(part)<=255:
            return False
    return True