def solution(arr, idx):
    n_arr = arr[idx:]
    if 1 in n_arr:
        answer = n_arr.index(1) + idx
    else:
        answer = -1
    return answer