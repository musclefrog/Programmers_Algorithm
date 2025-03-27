import math

def solution(fees, records):
    answer = []
    parking = {} # 입차 시간 저장
    use = {} # 차량별 누적 이용 시간
    
    for record in records:
        time, num, io = record.split(' ')
        h, m = map(int, time.split(':'))
        time_min = h * 60 +  m # 분으로 변환
        
        if io == 'IN': # 입차
            parking[num] = time_min
        else: # 출차
            if num in use:
                use[num] += time_min - parking[num]
            else:
                use[num] = time_min - parking[num]
            del parking[num] # 출차했으므로 삭제
    
    # 출차 기록이 없는 차량 23:59 처리 (즉, 1439분까지 주차)
    for num, in_time in parking.items():
        if num in use:
            use[num] += 1439 - in_time
        else:
            use[num] = 1439 - in_time
                
    # 차량 번호 기준 오름차순 정렬
    sorted_use = sorted(use.items())
    
    # 요금 계산
    for num, time in sorted_use:
        if time <= fees[0]: # 기본 시간 이하이면 기본 요금
            answer.append(fees[1])
        else: # 초과 요금 계산
            extra_time = time - fees[0]
            extra_fee = math.ceil(extra_time / fees[2]) * fees[3]
            answer.append(fees[1] + extra_fee)
    return answer