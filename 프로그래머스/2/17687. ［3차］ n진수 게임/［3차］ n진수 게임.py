def convert_base(num, base):
    digits = "0123456789ABCDEF"
    res = []
    
    if num == 0:
        return "0"

    while num > 0:
        res.append(digits[num % base])  # n진법 변환
        num //= base
    
    return ''.join(res[::-1])  # 역순으로 정렬 후 문자열로 변환

def solution(n, t, m, p):
    answer = []
    result = []
    num = 0
    
    # n진법 변환 문자열을 리스트에 저장
    while len(result) < (t * m):
        result.extend(convert_base(num, n))  # ✅ 직접 변환 함수 사용 (공백 문제 해결)
        num += 1

    # p번째 사람이 말할 숫자 추출
    for i in range(p-1, t*m, m):
        answer.append(result[i])  # ✅ 리스트 사용 후 join()

    return ''.join(answer)  # ✅ 문자열 결합 최적화