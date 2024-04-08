def solution(keyinput, board):
    answer = []
    x_lim = board[0] // 2
    y_lim = board[1] // 2
    move = {'left':(-1,0), 'right':(1,0), 'up':(0,1), 'down':(0,-1)}
    x, y = 0, 0
    for key in keyinput:
        dx, dy = move[key]
        if abs(x + dx) > x_lim or abs(y + dy) > y_lim:
            continue
        else:
            x, y = x + dx, y + dy
    return [x, y]