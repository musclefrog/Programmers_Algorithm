def func(n):
    to3_list = []
    answer = 0
    while n != 0:
        r = n % 3
        to3_list.append(r)
        n //= 3
    
    for i in range(len(to3_list)):
        if to3_list[i] == 0:
            continue
        else:
            answer += to3_list[i] * (3 ** (len(to3_list) - (i + 1)))
    return answer

def solution(n):
    return func(n)