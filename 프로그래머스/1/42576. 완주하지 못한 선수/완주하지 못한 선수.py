def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 해시 딕셔너리 생성
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
        
    # 해시의 합에서 완주자 해시를 빼면 미완주자의 해시만 남음
    for comp in completion:
        sumHash -= hash(comp)
    
    # 미완주자 해시의 key 값이 미완주자의 이름임
    return hashDict[sumHash]