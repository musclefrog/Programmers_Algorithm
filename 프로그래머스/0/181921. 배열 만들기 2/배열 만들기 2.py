def solution(l, r):
    answer = []
    for i in (range(l, r + 1)):
        if all(n in ['5', '0'] for n in str(i)):
            answer.append(i)
    return [-1] if len(answer) == 0 else answer