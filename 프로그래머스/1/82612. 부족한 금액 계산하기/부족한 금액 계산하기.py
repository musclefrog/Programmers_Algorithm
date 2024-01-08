def solution(price, money, count):
    needed = 0
    for i in range(1, count+1):
        needed += price * i
    return needed - money if money - needed < 0 else 0