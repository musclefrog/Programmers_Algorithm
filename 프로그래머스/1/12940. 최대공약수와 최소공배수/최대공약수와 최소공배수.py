import math

def LCM(n, m):
    return (n * m) / math.gcd(n, m)

def solution(n, m):
    return math.gcd(n, m), LCM(n, m)