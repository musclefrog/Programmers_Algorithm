from collections import deque

def solution(x, y, n):
    visited = [False] * (y + 1)
    queue = deque()
    queue.append((x, 0))  # (현재 숫자, 연산 횟수)
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == y:
            return cnt
        
        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y and not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, cnt + 1))
    
    return -1  # 만들 수 없는 경우