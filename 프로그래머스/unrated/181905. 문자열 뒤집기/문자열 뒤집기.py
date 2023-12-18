def solution(my_string, s, e):
    str_arr = list(my_string[s:e+1])
    answer = my_string.replace(my_string[s:e+1], ''.join(str_arr[::-1]))
    return answer