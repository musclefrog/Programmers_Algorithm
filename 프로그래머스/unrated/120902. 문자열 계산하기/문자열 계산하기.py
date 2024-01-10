def solution(my_string):
    arr = my_string.split(' ')
    answer = int(arr[0])
    for i, x in enumerate(arr):
        if i % 2 == 1:
            if x == '+':
                answer += int(arr[i+1])
            elif x == '-':
                answer -= int(arr[i+1])
    return answer