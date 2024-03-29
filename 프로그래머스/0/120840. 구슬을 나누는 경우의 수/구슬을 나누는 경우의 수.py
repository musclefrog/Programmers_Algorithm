def solution(balls, share):
    return fac(balls) / (fac(balls - share) * fac(share))

def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fac(x - 1)
    