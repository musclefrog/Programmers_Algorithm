def solution(my_string, indices):
    n_str = list(my_string)
    for i in indices:
        n_str[i] = ''
    return ''.join(n_str)