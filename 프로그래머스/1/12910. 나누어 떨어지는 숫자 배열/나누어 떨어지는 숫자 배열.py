def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    return answer if len(answer) != 0 else [-1]