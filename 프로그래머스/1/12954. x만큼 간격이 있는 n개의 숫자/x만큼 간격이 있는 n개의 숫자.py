def solution(x, n):
    answer = []
    add = x
    while len(answer) != n:
        answer.append(x)
        x += add
    return answer