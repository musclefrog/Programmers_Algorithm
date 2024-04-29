def solution(polynomial):
    coef, con = 0, 0
    for term in polynomial.split(' + '):
        if term.isdigit():
            con += int(term)
        else:
            coef = coef + 1 if term == 'x' else coef + int(term[:-1])
        
    if coef == 0: 
        return str(con)
    elif coef == 1:
        return "x + " + str(con) if con != 0 else "x"
    else:
        return f'{coef}x + {con}' if con != 0 else f'{coef}x'