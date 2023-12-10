def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        answer.append(arr[intervals[i][0]:intervals[i][1]+1])
    return [num for inner_list in answer for num in inner_list]