import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville) # scoville list -> heap 구조로
    
    while len(scoville) >= 2: # heappop() 했을 때 IndexError 방지
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return cnt
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2*2)
            cnt += 1
            
    if scoville[0] >= K: 
        return cnt
    else:
        return -1