def solution(numbers, k):
    answer = 0
    if len(numbers) / 2 < k:
        i = (k // (len(numbers) // 2)) + 1
        numbers = numbers * i
    return numbers[(k - 1) * 2]