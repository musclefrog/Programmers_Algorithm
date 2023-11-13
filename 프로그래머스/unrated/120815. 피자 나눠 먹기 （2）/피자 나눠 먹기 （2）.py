def solution(n):
    answer = 0
    for i in range(max(n, 6), (n*6)+1):
        if i % n == 0 and i % 6 == 0:
            lcm = i
            break
            
    answer = lcm // 6
    return answer