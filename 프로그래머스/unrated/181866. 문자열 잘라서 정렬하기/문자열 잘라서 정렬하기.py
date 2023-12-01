def solution(myString):
    answer = myString.split('x')
    answer.sort()
    return ' '.join(answer).split()