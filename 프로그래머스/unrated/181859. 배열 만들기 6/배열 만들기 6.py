def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
            continue
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
                continue
            else:
                stk.append(arr[i])
                i += 1
                continue
    return [-1] if len(stk) == 0 else stk