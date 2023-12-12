def solution(myString):
    for i in range(len(myString)):
        if ord(myString[i]) < 108:
            myString = myString.replace(myString[i], 'l')
    return myString