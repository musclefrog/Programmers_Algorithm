import math

def Base(n, k):
    result = []
    while n > 0:
        tmp = n % k
        n //= k
        result.append(str(tmp))
    result.reverse()
    return ''.join(result)

def isDecimal(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # 2를 제외한 짝수는 소수가 아님
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):  # 3부터 홀수만 확인
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    arr = Base(n, k).split('0')
    arr = [int(num) for num in arr if num]
    for num in arr:
        if isDecimal(num):
            answer += 1
    return answer