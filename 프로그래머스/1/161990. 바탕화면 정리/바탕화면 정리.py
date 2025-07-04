def solution(wallpaper):
    # 파일 좌표 저장
    file = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                file.append([i, j])
    
    # 위/아래/왼/오 끝 점 구하기
    max_y = file[0][0]
    min_y = file[0][0]
    max_x = file[0][1]
    min_x = file[0][1]
    
    for co in file:
        if co[0] > max_y:
            max_y = co[0]
        if co[0] < min_y:
            min_y = co[0]
        if co[1] > max_x:
            max_x = co[1]
        if co[1] < min_x:
            min_x = co[1]
    
    return [min_y, min_x, max_y + 1, max_x + 1]