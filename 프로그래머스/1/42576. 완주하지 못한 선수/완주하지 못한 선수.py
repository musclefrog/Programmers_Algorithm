def solution(participant, completion):
    dic = {}

    # 참가자 이름 등장 횟수 기록
    for p in participant:
        dic[p] = dic.get(p, 0) + 1

    # 완주자 이름 등장 횟수 차감
    for c in completion:
        dic[c] -= 1

    # 값이 1 이상인 key가 완주 못한 사람
    for key, value in dic.items():
        if value > 0:
            return key