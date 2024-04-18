# 재귀함수 정의
def find(data, p, step): # 사전을 기록할 배열, 현재 문자열, 현재 문자열 자릿수
    if step == 6: return # 종료 조건 명시: 최대 5글자 이므로
    data.append(p) # 사전 추가
    for c in ['A', 'E', 'I', 'O', 'U']: 
        find(data, ''.join([p, c]), step + 1) # 문자열을 모음 순서대로 합쳐서 다음 재귀 호출

def solution(word):
    answer = 0
    data = []
    find(data, '', 0)
    # 만들어진 사전에서 주어진 단어가 어디에 있는지 전체 탐색으로 찾음
    for i in range(len(data)):
        if data[i] == word:
            answer = i
            break
    return answer