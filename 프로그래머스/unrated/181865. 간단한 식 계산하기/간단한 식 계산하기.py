def solution(binomial):
    answer = 0
    bin_list = binomial.split()
    if bin_list[1] == '+':
        answer = int(bin_list[0]) + int(bin_list[2])
    elif bin_list[1] == '-':
        answer = int(bin_list[0]) - int(bin_list[2])
    elif bin_list[1] == '*':
        answer = int(bin_list[0]) * int(bin_list[2])
    return answer