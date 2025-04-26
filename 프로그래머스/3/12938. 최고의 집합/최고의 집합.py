def solution(n, s):
    # n개의 자연수로 합이 s인 집합을 만들 수 없는 경우
    if n > s:
        return [-1]
    # 최대한 균등하게 나누어 곱하는 것이 최대의 곱을 만듦
    else:
        num = s // n
        rem = s % n
        best = [num] * n
        
        for i in range(0, rem):
            best[i] += 1
        
        return sorted(best)