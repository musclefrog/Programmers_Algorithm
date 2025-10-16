import datetime


def solution(a, b):
    t = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    date = datetime.date(2016, a, b).weekday()
    
    return t[date]