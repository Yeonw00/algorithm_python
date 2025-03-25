# 리스트에서 짝수만 추출하기

# def filter_even_numbers(numbers:list) -> list :
#     result = []
#     for even_number in numbers:
#         if even_number % 2 == 0:
#             result.append(even_number)
#     return result

def filter_even_numbers(numbers:list) -> list:
    return [even_number for even_number in numbers if even_number % 2 == 0]