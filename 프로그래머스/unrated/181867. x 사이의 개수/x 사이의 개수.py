def solution(myString):
    answer = []
    n_str = []
    n_str = myString.split('x')
    for i in n_str:
        answer.append(len(i))
    return answer