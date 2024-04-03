def solution(arr):
    if len(arr) > len(arr[0]):
        for row in arr:
            for _ in range(len(arr)-len(row)):
                row.append(0)
    elif len(arr) < len(arr[0]):
        for _ in range(len(arr[0])-len(arr)):
            col = [0] * len(arr[0])
            arr.append(col)
    return arr