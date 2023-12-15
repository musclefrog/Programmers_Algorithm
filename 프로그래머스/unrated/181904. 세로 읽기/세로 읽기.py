def solution(my_string, m, c):
    answer = []
    n_str = [a for a in my_string]
    for i in range(0, len(n_str), m):
        answer.append(n_str[i + c - 1])
    return ''.join(answer)