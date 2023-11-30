def solution(x):
    arr = [int(i) for i in str(x)]
    x_sum = sum(arr)
    return True if x % x_sum == 0 else False