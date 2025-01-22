import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)): # 각 작업이 완료되는 일 수 계산
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    while days:
        count = 1  # 첫 번째 작업은 항상 포함
        first_day = days.pop(0)  # 첫 번째 작업의 완료 일수 기준

        # 나머지 작업 검사
        while days and days[0] <= first_day:
            days.pop(0)
            count += 1

        answer.append(count)  # 그룹화된 작업 수 추가
    return answer