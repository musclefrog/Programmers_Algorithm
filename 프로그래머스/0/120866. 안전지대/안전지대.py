def solution(board):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
   
    # 지뢰 설치
    boom = []
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                boom.append((i, j))
    
    # 지뢰 주변 위험지역으로 처리
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                board[nx][ny] = 1
                
    # 폭탄을 설치하지 않은 곳 카운팅
    cnt = 0
    for x in range(length):
        for y in range(length):
            if board[x][y] == 0:
                cnt += 1
    return cnt