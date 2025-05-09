def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(0, 4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if h_check in range(0, n) and w_check in range(0, n):
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    return count