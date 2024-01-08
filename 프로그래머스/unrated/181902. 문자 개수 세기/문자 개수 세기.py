def solution(my_string):
    answer = []
    alp_upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    alp_lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
    alp_list = alp_upper + alp_lower
    
    for alphabet in alp_list:
        answer.append(my_string.count(alphabet))
    return answer