def solution(A,B):
    answer = []
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer.append(A[i] * B[i])
    return sum(answer)