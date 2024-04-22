def gcd(x, y):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
        
def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd_num = gcd(numer, denom)
    return [numer / gcd_num, denom / gcd_num]