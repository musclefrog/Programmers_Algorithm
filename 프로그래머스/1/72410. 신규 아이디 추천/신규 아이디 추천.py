def solution(new_id):
    # 1 - 소문자화
    answer = new_id.lower()
    
    # 2 - 알파벳 소문자, 숫자, '-', '_', '.' 제외한 문자 제거
    tmp = []
    for letter in answer:
        if letter.isalpha() or letter.isdigit():
            tmp.append(letter)
        if letter in ['-', '_', '.']:
            tmp.append(letter)
        else:
            continue
    answer = tmp
    
    # 3 - 2번 이상 연속된 마침표(.)를 하나의 마침표로 치환
    tmp = [answer[0]]
    for i in range(1, len(answer)):
        if answer[i] == '.' and answer[i-1] == '.':
            continue
        else:
            tmp.append(answer[i])
    answer = tmp
    
    # 4 - 아이디의 처음에 위치한 '.' 제거
    if answer[0] == '.':
        answer.pop(0)
        
    # 5 - 빈 문자열이라면 "a"를 대입
    if not answer:
        answer = ["a"]
    
    # 6 - 길이가 16자 이상이면, 처음 15자를 제외한 나머지 문자 제거
    # + 제거 후 '.'가 끝에 위치한다면 끝의 '.' 제거
    answer = answer[:15]
    if answer[-1] == '.':
        answer.pop()
    
    # 7 - 길이가 2자 이하라면, 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[-1])
    
    return ''.join(answer)