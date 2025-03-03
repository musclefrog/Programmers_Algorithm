def solution(msg):
    answer = []
    dic = {chr(i + 65): i + 1 for i in range(26)}  # A~Z 사전 초기화
    index = 27  # 새로운 단어의 색인 번호
    i = 0  # msg에서 탐색할 위치

    while i < len(msg):
        w = msg[i]  # 현재 단어
        while i + 1 < len(msg) and w + msg[i + 1] in dic:  # 사전에 존재하는 가장 긴 단어 찾기
            i += 1
            w += msg[i]

        answer.append(dic[w])  # 사전에서 찾은 단어의 색인 번호 저장

        if i + 1 < len(msg):  # 새로운 단어를 사전에 추가
            dic[w + msg[i + 1]] = index
            index += 1

        i += 1  # 다음 문자로 이동

    return answer