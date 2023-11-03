def solution(hp):
    antA = hp // 5
    antB = hp % 5 // 3
    antC = hp % 5 % 3
    answer = antA + antB + antC
    return answer