def solution(keymap, targets):
    answer = []
    dict = {}
    
    # dict에 각 문자마다 최소로 자판 누르는 횟수를 저장
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in dict or dict[key] > i + 1:
                dict[key] = i + 1

    # 각 문자가 dict에 있으면 value를 cnt에 더해주고 없으면 -1
    # 각 target에 대한 cnt를 answer에 append
    for target in targets:
        cnt = 0
        for ch in target:
            if ch in dict:
                cnt += dict[ch]
            else:
                cnt = -1
                break
        answer.append(cnt)
    
    return answer