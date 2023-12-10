def solution(age):
    answer = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    num = [x for x in str(age)]
    for i in range(len(num)):
        answer.append(alphabet[int(num[i])])
    return ''.join(answer)