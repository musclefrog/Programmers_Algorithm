def solution(routes):
    # 차량의 진출 시점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    cameras = -30001  # 카메라 설치 위치 초기값 (진입 최소값보다 작게)
    answer = 0

    for route in routes:
        # 현재 차량의 진입 시점이 카메라보다 뒤라면 카메라가 이 차량을 못 찍음
        if route[0] > cameras:
            cameras = route[1]  # 새로운 카메라 설치
            answer += 1  # 카메라 개수 증가

    return answer
