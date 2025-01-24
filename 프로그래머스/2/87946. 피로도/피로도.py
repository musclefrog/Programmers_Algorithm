def solution(k, dungeons):
    max_count = 0 # 최대 탐험 가능한 던전 수
    
    def dfs(k, count, visited):
        nonlocal max_count
        max_count = max(max_count, count) # 최대 탐험 수 갱신
        
        # 모든 던전을 순회
        for i in range(len(dungeons)):
            # 방문하지 않았고, 현재 피로도가 최소 필요 피로도 이상인 경우
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True # 방문 표시
                # 다음 던전 탐험 (피로도 감소 및 탐험 수 증가)
                dfs(k - dungeons[i][1], count + 1, visited)
                visited[i] = False # 백트래킹: 방문 취소
    
    # 방문 여부 초기화
    visited = [False] * len(dungeons)
    
    # 모든 던전을 시작점으로 탐험 시도
    dfs(k, 0, visited)
    
    return max_count