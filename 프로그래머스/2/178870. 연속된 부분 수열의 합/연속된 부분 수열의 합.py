def solution(sequence, k):
    left = 0
    right = 0
    total = sequence[0]
    answer = []
    
    while left <= right and right < len(sequence):
        if total < k:
            right += 1
            if right < len(sequence):
                total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:
            answer.append([left, right])
            total -= sequence[left]
            left += 1
    
    return min(answer, key=lambda x: x[1]-x[0])