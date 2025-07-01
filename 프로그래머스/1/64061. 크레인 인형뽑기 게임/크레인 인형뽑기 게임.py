def solution(board, moves):
    answer = 0
    new_arr = [[] for _ in range(len(board))]
    
    # board 리스트 재배열
    size = len(board)
    for j in range(size):
        for i in range(size-1, -1, -1):
            if board[i][j] != 0:
                new_arr[j].append(board[i][j])
    
    # 인형 집어서 터트리기
    stack = []
    tmp = 0
    
    for move in moves:
        if new_arr[move-1]:
            tmp = new_arr[move-1].pop()
            stack.append(tmp)
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
    return answer