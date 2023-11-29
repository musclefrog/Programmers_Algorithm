def solution(s):
    answer = True
    s = s.lower()
    cnt_p = s.count('p')
    cnt_y = s.count('y')
    if cnt_p == cnt_y:
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer