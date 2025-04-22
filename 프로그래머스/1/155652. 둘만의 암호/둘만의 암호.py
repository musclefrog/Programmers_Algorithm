import string

def solution(s, skip, index):
    answer = []
    alphabet = list(string.ascii_lowercase)
    
    # skip에 따른 알파벳 배열 재정의
    for skip_ch in skip:
        alphabet.remove(skip_ch)
    
    alphabet_cnt = 26 - len(skip)
    
    # s의 각 문자 변경 후 answer에 append
    for ch in s:
        ch = alphabet[((alphabet.index(ch) + index) % alphabet_cnt)]
        answer.append(ch)

    return ''.join(answer)