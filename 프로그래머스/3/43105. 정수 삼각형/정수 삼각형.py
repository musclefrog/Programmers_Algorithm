def solution(triangle):
    # 삼각형의 마지막 행부터 거꾸로 올라가며 최댓값을 갱신
    for i in range(len(triangle)-2, -1, -1): # 아래에서 두 번째 줄부터 위로
        for j in range(len(triangle[i])):
            # 아래 행의 두 개 중 큰 값 선택해서 현재 위치 업데이트
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    # 최종적으로 꼭대기(triangle[0][0])에 최댓값이 저장됨        
    return triangle[0][0]