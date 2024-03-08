def toOne(num_list):
    answer = 0
    for num in num_list:
        cnt = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num - 1) // 2
            cnt += 1
        answer += cnt
    return answer

def solution(num_list):
    return toOne(num_list)