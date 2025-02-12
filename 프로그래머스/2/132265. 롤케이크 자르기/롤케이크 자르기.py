def solution(topping):
    answer = 0
    left_set = set()  # 왼쪽 부분의 토핑 종류
    right_count = {}  # 오른쪽 부분의 토핑 개수 저장
    
    # 오른쪽 부분의 토핑 개수 미리 계산
    # topping 리스트를 처음부터 끝까지 돌면서 각 토핑이 몇 번 등장하는지를 저장
    for t in topping:
        right_count[t] = right_count.get(t, 0) + 1 # 기존에 존재하는 값이면 +1 증가, 없다면 0에서 시작하여 1로 설정.
    
    # 왼쪽에서 하나씩 추가하면서 오른쪽에서 제거
    for i in range(len(topping) - 1):
        left_set.add(topping[i])  # 왼쪽에 추가
        right_count[topping[i]] -= 1  # 오른쪽에서 제거
        
        if right_count[topping[i]] == 0:
            del right_count[topping[i]]  # 개수가 0이면 삭제
        
        # 왼쪽과 오른쪽의 토핑 종류 개수가 같으면 증가
        if len(left_set) == len(right_count):
            answer += 1
    
    return answer