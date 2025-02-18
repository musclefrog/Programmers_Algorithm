def solution(dirs):
    cur = (0, 0)
    record = set()
    
    for o in dirs:
        if o == 'U':
            update = (cur[0], cur[1] + 1)
        elif o == 'D':
            update = (cur[0], cur[1] - 1)
        elif o == 'R':
            update = (cur[0] + 1, cur[1])
        elif o == 'L':
            update = (cur[0] - 1, cur[1])
        
        # 경계를 벗어나면 무시
        if not(-5 <= update[0] <= 5 and -5 <= update[1] <= 5):
            continue
            
        # 길을 양방향으로 동일하게 저장
        record.add(tuple(sorted([cur, update])))
                                 
        # 위치 업데이트
        cur = update
                                 
    return len(record)