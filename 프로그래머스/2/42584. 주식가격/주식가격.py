from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        cnt = 0
        x = queue.popleft()
        for i in queue:
            if x <= i:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer