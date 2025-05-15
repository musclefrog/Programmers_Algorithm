from functools import cmp_to_key

def my_compare (a, b):
    if a + b > b + a:
        return -1
    if a + b == b + a:
        return 0
    else:
        return 1

def solution(numbers):
    numbers = [str(num) for num in numbers]
    sorted_list = sorted(numbers, key=cmp_to_key(my_compare))
    
    result = ''.join(sorted_list)
    return '0' if result[0] == '0' else result