def solution(m, n, puddles):
    MOD = 1000000007
    # DP 배열 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    # 웅덩이 표시
    for x, y in puddles:
        dp[y][x] = -1

    # DP 점화식으로 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0  # 웅덩이는 0으로 초기화
                continue
            # 왼쪽(dp[i][j-1]) + 위쪽(dp[i-1][j])에서 오는 경로 수를 더함
            if i > 1:
                dp[i][j] += dp[i - 1][j]
            if j > 1:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD

    return dp[n][m]