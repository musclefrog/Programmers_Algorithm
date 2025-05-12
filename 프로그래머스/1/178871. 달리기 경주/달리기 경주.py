def solution(players, callings):
    pos = {player: i for i, player in enumerate(players)}  # 이름 → 위치 매핑

    for call in callings:
        i = pos[call]
        players[i], players[i-1] = players[i-1], players[i]  # 자리 바꾸고
        # 새로 바뀐 위치 갱신
        pos[players[i]] = i
        pos[players[i-1]] = i - 1

    return players
