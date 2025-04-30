def solution(A, B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    
    p = 0
    
    for i in range(len(A)):
        for j in range(p, len(B)):
            if A[i] < B[j]:
                answer += 1
                p = j + 1
                break
                
    return answer