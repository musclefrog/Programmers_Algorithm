def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i].isdigit(): continue
            answer = False
    else: 
        answer = False
    return answer