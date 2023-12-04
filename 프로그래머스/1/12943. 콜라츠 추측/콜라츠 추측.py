def solution(num):
    cnt = 0
    if num == 1:
        answer = 0
    else:
        while num != 1:
            cnt += 1
            if num % 2 == 0:
                num //= 2
            elif num % 2 == 1:
                num = num * 3 + 1
        answer = cnt
    if cnt >= 500:
        answer = -1
    return answer