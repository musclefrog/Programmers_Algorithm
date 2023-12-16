def solution(board, k):
    arr = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                arr.append(board[i][j])
    return sum(arr)