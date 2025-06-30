def solution(survey, choices):
    answer = ''
    score = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += 4 - choices[i]  # 왼쪽 지표 점수 누적
        elif choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4  # 오른쪽 지표 점수 누적
    
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer