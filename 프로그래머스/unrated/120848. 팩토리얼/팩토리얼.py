def fac(num):
    if num == 1: return 1
    return num * fac(num-1)

def solution(n):
    for num in range(1, 11):
        if n >= fac(num):
            answer = num
    return answer