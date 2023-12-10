def solution(order):
    answer = 0
    num = [x for x in str(order)]
    for i in range(len(num)):
        if num[i] != '0' and int(num[i]) % 3 == 0:
            answer += 1
    return answer