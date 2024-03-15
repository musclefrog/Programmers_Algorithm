def solution(arr):
    if arr.count(2) == 0:
        return [-1]
    else:
        re_arr = list(reversed(arr))
        i = arr.index(2)
        j = len(arr) - re_arr.index(2)
        return arr[i:j]