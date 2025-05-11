def solution(data, ext, val_ext, sort_by):
    dic = {"code":  0, "date": 1, "maximum": 2, "remain": 3}
    
    ext_idx = dic[ext]
    sort_idx = dic[sort_by]
    
    # 조건을 만족하는 행만 필터링
    filtered = [row for row in data if row[ext_idx] < val_ext]
    
    # 정렬
    filtered.sort(key = lambda x: x[sort_idx])
    
    return filtered