import math

def solution(n, stations, w):
    answer = 0
    coverage = 2*w + 1  # 기지국 하나가 커버할 수 있는 범위

    start = 1  # 처음 아파트 번호부터 시작
    for station in stations:
        left = station - w  # 이 기지국이 덮기 시작하는 지점
        if start < left:
            gap = left - start  # 안 덮인 구간 길이
            answer += math.ceil(gap / coverage)
        start = station + w + 1  # 다음 탐색 시작 위치 (현재 기지국 오른쪽 끝 다음칸)

    # 마지막 기지국 이후도 덮여야 한다면
    if start <= n:
        gap = n - start + 1
        answer += math.ceil(gap / coverage)

    return answer
