def solution(numbers):
    all_sum = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            all_sum.append(numbers[i] + numbers[j])
    answer = sorted(list(set(all_sum)))
    return answer