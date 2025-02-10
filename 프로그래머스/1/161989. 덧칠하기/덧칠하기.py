from collections import deque

def solution(n, m, section):
    cnt = 0
    section = deque(section)  # `deque`로 변환

    while section:
        start = section.popleft()  # ✅ 가장 작은 값 가져오기 (O(1))
        while section and section[0] < start + m:  
            section.popleft()  # ✅ m 범위 안에 포함되는 값 제거 (O(1))
        cnt += 1  

    return cnt