def solution(numbers, hand):
    answer = []
    left_n = [1, 4, 7, '*']
    middle_n = [2, 5, 8, 0]
    right_n = [3, 6, 9, '#']
    now_L, now_R = '*', '#'
    distance_L, distance_R = 0, 0
    for number in numbers:
        # 왼쪽 열, 오른쪽 열에 있는 수는 무조건 해당 손으로 입력
        if number in left_n:
            now_L = number
            answer.append('L')
        elif number in right_n:
            now_R = number
            answer.append('R')
        # number가 중간 열이라면
        else:
            # 현재 왼손이 왼쪽 열에 있을 경우 거리 구하기
            if now_L in left_n:
                distance_L = abs(middle_n.index(number) - left_n.index(now_L)) + 1
            # 현재 왼손이 중간 열에 있을 경우 거리 구하기
            elif now_L in middle_n:
                distance_L = abs(middle_n.index(number) - middle_n.index(now_L))
            # 현재 오른손이 오른쪽 열에 있을 경우 거리 구하기
            if now_R in right_n:
                distance_R = abs(middle_n.index(number) - right_n.index(now_R)) + 1
            # 현재 오른손이 중간 열에 있을 경우 거리 구하기
            elif now_R in middle_n:
                distance_R = abs(middle_n.index(number) - middle_n.index(now_R))
            # 왼쪽에서의 거리와 오른쪽에서의 거리가 같다면
            if distance_L == distance_R:
                # 어느 손 잡인지 판단해서 입력
                if hand == "right":
                    now_R = number
                    answer.append('R')
                elif hand == "left":
                    now_L = number
                    answer.append('L')
            # 오른손에서 더 가까울 때
            elif distance_L > distance_R:
                now_R = number
                answer.append('R')
            # 왼손에서 더 가까울 때
            else:
                now_L = number
                answer.append('L')
    return ''.join(answer)