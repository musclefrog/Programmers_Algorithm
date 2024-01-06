def solution(order):
    pay = 0
    for menu in order:
        if "americano" in menu or "anything" in menu:
            pay += 4500
        elif "cafelatte" in menu:
            pay += 5000
    return pay