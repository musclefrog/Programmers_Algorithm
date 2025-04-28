from collections import Counter

def solution(X, Y):
    arr = []
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    for num in count_X:
        if num in count_Y:
            arr.extend([num] * min(count_X[num], count_Y[num]))

    
    if not arr:
        return '-1'
    
    arr.sort(key=int, reverse=True)
    
    if arr[0] == '0':
        return '0'
    
    return ''.join(arr)