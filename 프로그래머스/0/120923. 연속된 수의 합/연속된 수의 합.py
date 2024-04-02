def solution(num, total):
    answer = []
    i = (total - sum(range(num))) / num
    for _ in range(num):
        answer.append(i)
        i += 1
    return answer