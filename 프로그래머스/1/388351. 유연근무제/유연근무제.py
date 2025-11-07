def solution(schedules, timelogs, startday):
    answer = 0
    
    # 출근 마감 시간 구하기
    limit_time = []
    
    for s in schedules:
        tmp = s + 10
        if tmp % 100 >= 60:
            tmp += 40
        limit_time.append(tmp)
        
    # 주말 인덱스 계산
    weekend = [(6 - startday) % 7, (7 - startday) % 7]
    
    # 직원별 정상 근무 여부 확인
    for i in range(len(schedules)):
        ok = True
        for j in range(7):
            if j in weekend:
                continue
            if timelogs[i][j] > limit_time[i]:
                ok = False
                break
        if ok:
            answer += 1
    
    return answer