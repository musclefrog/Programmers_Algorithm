def solution(order):
    arr = list(range(1, len(order) + 1))  # [1, 2, 3, ..., n]
    stack = []
    truck = 0
    index = 0  # order 배열의 인덱스 (현재 넣어야 할 컨테이너 번호)

    for box in arr:  # 주 컨베이어 벨트에서 컨테이너 하나씩 확인
        if box == order[index]:  # 바로 트럭으로 이동 가능
            truck += 1
            index += 1
            # 보조 컨테이너 벨트에서 적재할 수 있는지 확인
            while stack and stack[-1] == order[index]:  
                stack.pop()
                truck += 1
                index += 1
        else:  # 트럭으로 바로 못 가면 보조 컨베이어 벨트에 저장
            stack.append(box)

    return truck