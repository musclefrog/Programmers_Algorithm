def solution(arr):
    answer = [0, 0]  # [0의 개수, 1의 개수]

    def compress(x, y, size):
        # 현재 영역의 첫 번째 값을 기준으로
        num = arr[x][y]
        
        # 해당 영역이 전부 같은 숫자인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != num:
                    # 다르면 4등분해서 재귀 호출
                    half = size // 2
                    compress(x, y, half)  # 왼쪽 위
                    compress(x, y + half, half)  # 오른쪽 위
                    compress(x + half, y, half)  # 왼쪽 아래
                    compress(x + half, y + half, half)  # 오른쪽 아래
                    return
        
        # 전부 같다면 해당 숫자의 개수만 +1
        answer[num] += 1

    # 전체 배열에서 시작
    compress(0, 0, len(arr))
    return answer
