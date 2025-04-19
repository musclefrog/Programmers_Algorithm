def solution(s):
    answer = 0
    i = 0

    while i < len(s):
        x = s[i]
        count_x = 1
        count_other = 0
        j = i + 1

        while j < len(s):
            if s[j] == x:
                count_x += 1
            else:
                count_other += 1
            if count_x == count_other:
                break
            j += 1

        answer += 1
        i = j + 1  # 다음 구간으로 이동

    return answer
