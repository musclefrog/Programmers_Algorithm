def solution(myStr):
    answer = []
    myStr = list(myStr)
    for i in myStr:
        if i == 'a':
            temp = i.replace('a', ' ')
            answer.append(temp)
        elif i == 'b':
            temp = i.replace('b', ' ')
            answer.append(temp)
        elif i == 'c':
            temp = i.replace('c', ' ')
            answer.append(temp)
        else:
            answer.append(i)
    
    result = ''.join(answer).split()
    
    return result if len(result) > 0 else ["EMPTY"]