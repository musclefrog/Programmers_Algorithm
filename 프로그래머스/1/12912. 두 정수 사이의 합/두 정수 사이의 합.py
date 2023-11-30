def solution(a, b):
    answer = 0
    num_arr = [a, b]
    for num in range(min(num_arr), max(num_arr)+1):
        answer += num
    return a if a == b else answer