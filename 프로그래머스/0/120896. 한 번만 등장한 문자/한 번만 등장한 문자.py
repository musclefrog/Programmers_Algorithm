def solution(s):
    answer = []
    s = list(s)
    s.sort()
    for i in s:
        if s.count(i) == 1:
            answer.append(i)
    return ''.join(answer)