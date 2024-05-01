def solution(food):
    arr = []
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            arr.append(str(i))
    arr_reversed = reversed(arr)
    arr.append("0")
    arr += arr_reversed
    return ''.join(arr)