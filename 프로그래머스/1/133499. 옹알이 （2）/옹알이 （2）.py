def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for bab in babbling: # bab: “yemawoo”
        said = ''
        tmp = bab
        while tmp: # 남은 문자열이 없을 때까지 반복
            for word in words:
                if tmp.startswith(word) and said != word: # 연속된 같은 단어는 X
                    tmp = tmp[len(word):] # 단어를 잘라서 제거
                    said = word # 마지막으로 말한 단어 저장
                    break # 새로운 단어를 찾기 위해 for문 다시 시작
            else:
                 break # for문에서 break 없이 끝났다면 더 이상 진행 불가 → while 종료
        if not tmp:
            answer += 1
    return answer