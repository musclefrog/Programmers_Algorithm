def solution(skill, skill_trees):
    answer = 0
    skill_arr = list(skill)
    
    for input in skill_trees:
        succeed = True
        arr = list(input)
        stack = []
        
        
        for i in range(len(arr)):
            # arr의 원소가 skill_arr 안에 있을 경우에만 stack에 push 한다.
            if arr[i] in skill_arr:
                stack.append(arr[i])
                # stack이 skill_arr[:len(stack)]과 일치하면 계속하고, 아니면 succeed를 False로 바꾸고 break 한다.
                if stack == skill_arr[:len(stack)]:
                    continue
                else:
                    succeed = False
                    break
        # 해당 input이 succeed = True라면 answer에 1을 더한다.
        if succeed:
            answer += 1
    return answer