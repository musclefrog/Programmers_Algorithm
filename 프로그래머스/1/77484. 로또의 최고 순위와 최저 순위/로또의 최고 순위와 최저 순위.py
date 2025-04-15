def solution(lottos, win_nums):
    match, zero = 0, 0
    for x in lottos:
        if x != 0:
            for y in win_nums:
                if x == y:
                    match += 1
        else:
            zero += 1
            
    max_match = match + zero
    min_match = match
    
    if min_match == 0:
        min_rank = 6
    else:
        min_rank = 7 - min_match
    
    if max_match == 0:
        max_rank = 6
    else:
        max_rank = 7 - max_match
    
    return [max_rank, min_rank]