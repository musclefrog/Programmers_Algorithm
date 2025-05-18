from itertools import permutations
import math

# 소수 판별 함수
def isPrimeNumber(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    
    # numbers 리스트의 모든 조합을 구함
    for cnt in range(1, len(numbers) + 1):
        arr.extend(map(''.join, list(permutations(numbers, cnt))))
        
    # 리스트 형 변환
    arr = list(map(int, arr))
    
    # 중복 숫자 제거
    wtf = set(arr)
    
    # 소수 판별
    for num in wtf:
        if isPrimeNumber(num):
            answer += 1
    
    return answer