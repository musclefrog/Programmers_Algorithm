def solution(files):
    arr = []
    for file in files:
        i = 0
        head = ''
        number = ''
        tail = ''
        
        # head 부분 처리
        while i < len(file) and (file[i].isalpha() or file[i] in [' ', '.', '-']):
            head += file[i]
            i += 1
        
        # number 부분 처리
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1
            
        # 나머지는 tail
        tail = file[i:]
        
        arr.append((head, number, tail))
        
    # head는 대소문자 무시하고 비교하도록, number는 정수로 바꾸어 비교하도록 한다.
    arr.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(x) for x in arr]