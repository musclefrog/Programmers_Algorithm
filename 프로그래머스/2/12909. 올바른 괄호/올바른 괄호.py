def solution(s):
    stack = []
    for i in s:
        if i == '(':    # '('인 경우 일단 넣음
            stack.append(i)
        else:
            if stack == []:     # ')'로 시작하면 꽝
                return False
            else:
                stack.pop()     # stack이 비지 않았으면 ')'와 짝지어 빼냄
    return stack == []  # 짝지어진 괄호는 모두 빠져 나가고, 만약 남아있다면 짝지어지지 않은 것이기 때문에 False를 리턴