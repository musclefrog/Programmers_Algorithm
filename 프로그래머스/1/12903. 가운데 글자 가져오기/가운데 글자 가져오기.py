def solution(s):
    idx = len(s) // 2
    return s[idx] if len(s) % 2 == 1 else s[idx-1:idx+1]