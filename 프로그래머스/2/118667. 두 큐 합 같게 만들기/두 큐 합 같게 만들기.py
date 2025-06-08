from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 각 큐의 총합 계산
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2
    
    # 총합이 홀수면 둘로 나눌 수 없으므로 -1 리턴
    if total % 2 != 0:
        return -1
    
    target = total // 2
    cnt = 0
    
    # 최악의 경우 큐 길이의 3배까지 반복 (안 되는 경우 방지)
    max_count = len(q1) * 3
    
    while cnt <= max_count:
        if sum1 == target:
            return cnt  # 목표 달성하면 종료
        
        if sum1 > target:
            # q1의 값 하나를 q2로 옮김
            x = q1.popleft()
            sum1 -= x
            q2.append(x)
            sum2 += x
        else:
            # q2의 값 하나를 q1으로 옮김
            x = q2.popleft()
            sum2 -= x
            q1.append(x)
            sum1 += x
        
        cnt += 1
    
    return -1