import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0  # 남은 작업량이 n 이하이면 모두 없앨 수 있음 (야근 피로도 = 0)

    # 최대 힙을 만들기 위해 모든 값을 음수로 변환
    works = [-w for w in works]
    heapq.heapify(works)  # O(k) (works 크기만큼 힙 생성)

    for _ in range(n):
        max_work = heapq.heappop(works)  # O(log k) (가장 큰 값 꺼내기)
        if max_work == 0:
            break  # 더 이상 줄일 작업이 없으면 종료
        heapq.heappush(works, max_work + 1)  # O(log k) (값 감소 후 다시 삽입)

    return sum(w ** 2 for w in works)  # 남은 작업량 제곱의 합 계산