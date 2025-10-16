import datetime

x, y = map(int, input().split())

def getDay(x, y):
	t = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	date = datetime.date(2007, x, y).weekday()
	return t[date]

print(getDay(x, y))