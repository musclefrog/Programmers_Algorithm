def solution(s):
    answer = 0
    num = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    while s.isdigit() != True:
        for n in num:
            if n in s:
                s = s.replace(n, num[n])
    return int(s)