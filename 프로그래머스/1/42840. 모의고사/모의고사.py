def solution(answers):
    answer = []
    result = []
    
    test = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for t in test:
        cnt = 0
        for i in range(len(answers)):
            if t[i % len(t)] == answers[i]:
                cnt += 1
        result.append(cnt)
        
    for i in range(3):
        if result[i] == max(result):
            answer.append(i+1)
    
    return answer