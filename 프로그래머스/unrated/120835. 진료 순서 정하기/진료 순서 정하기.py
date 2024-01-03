def solution(emergency):
    answer = []
    sorted_arr = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        order = sorted_arr.index(emergency[i]) + 1
        answer.append(order)
    return answer