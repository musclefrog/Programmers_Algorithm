from collections import deque

def solution(priorities, location):
    queue = deque([(value, idx) for idx, value in enumerate(priorities)])
    answer = 0
    
    while queue:
        cur = queue.popleft()
        if any(cur[0] < item[0] for item in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer