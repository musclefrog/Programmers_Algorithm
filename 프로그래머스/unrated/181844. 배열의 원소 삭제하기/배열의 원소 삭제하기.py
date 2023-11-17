def solution(arr, delete_list):
    answer = []
    for arr_num in arr:
        if arr_num not in delete_list:
            answer.append(arr_num)
    return answer