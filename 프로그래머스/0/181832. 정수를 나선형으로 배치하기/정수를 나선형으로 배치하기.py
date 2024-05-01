def solution(n):
    arr = [[0] * n for _ in range(n)]
    cnt = 1
    startRow = 0
    endRow = n - 1
    startCol = 0
    endCol = n - 1
    
    while cnt <= n * n:
        for i in range(startCol, endCol+1):
            arr[startRow][i] = cnt
            cnt += 1
        startRow += 1
        for i in range(startRow, endCol+1):
            arr[i][endCol] = cnt
            cnt += 1
        endCol -= 1
        for i in range(endCol, startCol-1, -1):
            arr[endRow][i] = cnt
            cnt += 1
        endRow -= 1
        for i in range(endRow, startRow-1, -1):
            arr[i][startCol] = cnt
            cnt += 1
        startCol += 1
    return arr