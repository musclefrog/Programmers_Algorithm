def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for j in range(n):
            if computers[node][j] == 1 and not visited[j]:
                dfs(j)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer