def solution(m, n, board):
    answer = 0
    
    # 2D board 문자열 리스트를 2차원 리스트로 변환 후 90도 회전
    rotated = [list(col) for col in zip(*board[::-1])]
    
    while True:
        delete = set()
        for i in range(n-1):  # 열 개수
            for j in range(m-1):  # 행 개수
                block = rotated[i][j]
                if block == ' ':
                    continue
                if (block == rotated[i+1][j] == rotated[i][j+1] == rotated[i+1][j+1]):
                    delete |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)}
        
        if not delete:
            break

        # 블록 지우기
        for x, y in delete:
            rotated[x][y] = ' '
        
        # 블록 떨어뜨리기 (열마다)
        for i in range(n):
            new_col = [c for c in rotated[i] if c != ' ']
            rotated[i] = new_col + [' '] * (m - len(new_col))
        
        # 정답은 지운 칸의 개수 누적
        answer += len(delete)
    
    return answer