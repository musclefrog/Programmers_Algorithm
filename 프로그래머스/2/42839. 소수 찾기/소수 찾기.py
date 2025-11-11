from itertools import permutations

# 소수 판별 함수
def checkPrime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    num = []
    
    # 순열 만들기
    for i in range(1, len(numbers)+1):
        num.append(list(permutations(numbers, i)))
    num = [int(''.join(y)) for x in num for y in x] # 2차원 배열 flatten
    
    # 소수 판별
    for i in num:
        if checkPrime(i):
            answer.append(i)
            
    return len(set(answer))