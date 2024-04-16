def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while num > answer[-1]:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)