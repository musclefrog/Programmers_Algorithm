def solution(record):
    answer = []
    # 입력 처리
    input = []
    for rec in record:
        input.append(rec.split(' '))

    name_dict = {} # uid와 name을 맵핑하는 딕셔너리
    message = [] # 출력 결과를 넣을 리스트
    
    for arr in input:
        if arr[0] == "Enter":
            name_dict[arr[1]] = arr[2]
            message.append([arr[1], "님이 들어왔습니다."])
        if arr[0] == "Leave":
            message.append([arr[1], "님이 나갔습니다."])
        if arr[0] == "Change":
            name_dict[arr[1]] = arr[2]
    
    for mes in message:
        answer.append([name_dict[mes[0]], mes[1]])
    
    return [''.join(x) for x in answer]