import re

def solution(dartResult):
    # 정규 표현식: 점수(숫자) + 보너스(S, D, T) + 옵션(*, #) (옵션은 있을 수도 있고 없을 수도 있음)
    pattern = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    stack = []
    
    for i, (score, bonus, option) in enumerate(pattern):
        score = int(score)  # 점수 변환
        
        # 보너스 점수 적용
        if bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3
        
        # 옵션 처리
        if option == '*':
            score *= 2
            if stack:  # 이전 점수도 2배
                stack[-1] *= 2
        elif option == '#':
            score *= -1
        
        stack.append(score)
    
    return sum(stack)  # 최종 점수 합산