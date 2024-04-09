def solution(d, budget):
    answer, i = 0, 0
    needed = sum(d)
    d_sort = sorted(d)
    if needed <= budget:
        answer = len(d)
    else:
        while needed > budget:
            i += 1
            needed -= d_sort[len(d_sort)-i]
        answer = len(d) - i
    return answer