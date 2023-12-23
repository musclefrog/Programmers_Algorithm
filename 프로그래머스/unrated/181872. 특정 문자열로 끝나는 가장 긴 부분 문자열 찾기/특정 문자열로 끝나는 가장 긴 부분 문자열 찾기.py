def solution(myString, pat):
    idx = myString.rfind(pat) + len(pat)-1
    return myString[:idx+1]