def solution(babbling):
    answer = 0
    pronounce = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for pro in pronounce:
            while bab.find(pro) >= 0:
                bab = bab.replace(pro, ' ')
                if bab.replace(' ', '') == '': 
                    answer += 1
    return answer