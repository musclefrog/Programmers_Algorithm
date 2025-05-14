def solution(numbers):
    answer = []
    for num in numbers:
        # num이 짝수일 때
        if num % 2 == 0:
            answer.append(num + 1)
        # num이 홀수일 때
        else:
            b = '0' + bin(num)[2:]  # 앞에 0 붙여서 예외 처리
            idx = b.rfind('01')    # 뒤에서부터 '01'을 찾아서
            b = list(b)
            b[idx] = '1'
            b[idx + 1] = '0'
            answer.append(int(''.join(b), 2))
    return answer