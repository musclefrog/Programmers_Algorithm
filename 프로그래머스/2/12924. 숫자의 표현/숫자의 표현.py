def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        sum = 0
        while sum < n:
            sum += i
            i += 1
            if sum == n:
                cnt += 1
    return cnt