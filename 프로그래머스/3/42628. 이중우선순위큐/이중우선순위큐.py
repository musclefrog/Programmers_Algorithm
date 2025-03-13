import heapq

def solution(operations):
    queue = []
    for op in operations:
        [order, num] = op.split()
        num = int(num)
        if order == 'D':
            if queue:
                if num == -1:
                    heapq.heappop(queue)
                else: # num == 1
                    max_val = heapq.nlargest(1, queue)[0] # 현재 최대값 찾기
                    queue.remove(max_val) # 최대값 리스트에서 제거
                    heapq.heapify(queue) # 힙 재정렬
        else: # order == 'I'
            heapq.heappush(queue, num) # queue에 num 삽입
    
    if queue: # queue가 비어있지 않을 때
        return [max(queue), min(queue)]
    else: # queue가 비어있을 때
        return [0, 0]