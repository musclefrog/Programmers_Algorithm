def solution(array, n):
    diff = []
    array.sort()
    for i in array:
        diff.append(abs(i - n))
    answer = [array[diff.index(min(diff))]]
    return min(answer) if len(answer) > 1 else answer[0]