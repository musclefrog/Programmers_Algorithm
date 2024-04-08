def solution(dots):
    dot_x = []
    dot_y = []
    for x, y in dots:
        dot_x.append(x)
        dot_y.append(y)
    return abs(max(dot_x) - min(dot_x)) * abs(max(dot_y) - min(dot_y))