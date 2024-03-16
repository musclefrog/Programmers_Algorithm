def solution(quiz):
    answer = ''
    result = []
    for op in quiz:
        el = op.split()
        if el[1] == '+':
            if int(el[0]) + int(el[2]) == int(el[4]):
                answer = "O"
            else:
                answer = "X"
        elif el[1] == '-':
            if int(el[0]) - int(el[2]) == int(el[4]):
                answer = "O"
            else:
                answer = "X"
        result.append(answer)
    return result