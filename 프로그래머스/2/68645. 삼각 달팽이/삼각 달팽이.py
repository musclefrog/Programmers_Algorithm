def solution(n):
    # 삼각형 모양의 배열 만들기
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    
    x,y = -1, 0
    num = 1
    
    # 좌표에 따른 값 대입
    for i in range(n):
        for j in range(i, n):
            # 아래로 이동하는 경우
            if i%3 == 0:
                x += 1
            # 오른쪽으로 이동하는 경우
            elif i%3 == 1:
                y += 1
            # 왼쪽 위로 이동하는 경우
            else:
                x -= 1
                y -= 1
            
            answer[x][y] = num  # 이동한 좌표에 숫자 대입
            num += 1
    
    return sum(answer, [])