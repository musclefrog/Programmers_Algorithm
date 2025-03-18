from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        cnt = 0
        x = queue.popleft()
        for i in queue:
            if x <= i: # 뒤에 남은 숫자가 같거나 작으면 cnt += 1
                cnt += 1
            else: # 뒤에 남은 숫자가 같거나 작지 않을 경우 cnt += 1 하고 break
                cnt += 1
                break
        answer.append(cnt)
    return answer