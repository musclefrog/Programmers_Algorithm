def solution(s):
    s = s[2:-2].split('},{')
    s_set = []
    for nums in s:
        s_set.append(list(map(int, nums.split(','))))
        
    s_set.sort(key=len)
    answer = s_set[0]
        
    for i in range(0, len(s_set) - 1):
        answer.append(list(set(s_set[i+1]) - set(s_set[i]))[0])
    
    return answer