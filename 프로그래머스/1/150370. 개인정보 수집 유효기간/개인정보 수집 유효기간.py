import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    td = datetime.datetime.strptime(today, '%Y.%m.%d')
    
    terms_dict = {}
    
    for term in terms:
        x, y = term.split(' ')
        terms_dict[x] = int(y)
    
    for i in range(len(privacies)):
        stored_date, term_type = privacies[i].split(' ')
        date1 = datetime.datetime.strptime(stored_date, '%Y.%m.%d')
        date2 = date1 + relativedelta(months=terms_dict[term_type]) - datetime.timedelta(days=1)
        
        if date2 < td:
            answer.append(i+1)
    
    return answer