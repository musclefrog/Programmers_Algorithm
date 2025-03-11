def solution(numbers):
    answer = [-1] * len(numbers)  # 기본값 -1로 초기화
    stack = []  # 인덱스를 저장하는 스택

    for i in range(len(numbers) - 1, -1, -1):  # 역순으로 순회
        while stack and stack[-1] <= numbers[i]:  
            stack.pop()  # 현재 값보다 작은 값들은 제거 (필요 없는 값)

        if stack:  # 스택에 남아 있는 값 중 가장 가까운 큰 수
            answer[i] = stack[-1]

        stack.append(numbers[i])  # 현재 값을 스택에 저장

    return answer