def solution(rank, attendance):
    cnt = 1
    top = []
    while cnt <= len(rank):
        if len(top) == 3:
            break
        i = rank.index(cnt)
        if attendance[i] == True:
            top.append(i)
        rank[i] = 0
        cnt += 1
    return 10000 * top[0] + 100 * top[1] + top[2]