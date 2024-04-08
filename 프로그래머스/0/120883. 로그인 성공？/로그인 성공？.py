def solution(id_pw, db):
    answer = "fail"
    for info in db:
        if id_pw[0] in info:
            if id_pw[1] == info[1]:
                answer = "login"
            else:
                answer = "wrong pw"
    return answer