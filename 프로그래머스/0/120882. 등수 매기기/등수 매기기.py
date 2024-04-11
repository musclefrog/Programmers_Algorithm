def solution(score):
    score_avg = []
    for EnM in score:
        score_avg.append((EnM[0] + EnM[1]) / 2)
    sort_score = sorted(score_avg, reverse=True)
    answer = [sort_score.index(s) + 1 for s in score_avg]
    return answer