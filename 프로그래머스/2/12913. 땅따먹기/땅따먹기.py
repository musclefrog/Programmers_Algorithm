def solution(land):
    for i in range(1, len(land)):
        for j in range(4):  # 4개의 열을 탐색
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])  # 이전 행에서 같은 열을 제외한 최대값 더하기
    
    return max(land[-1])  # 마지막 행에서 가장 큰 값 반환