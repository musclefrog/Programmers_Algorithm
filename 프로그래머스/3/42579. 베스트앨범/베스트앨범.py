def solution(genres, plays):
    # 1. 장르별 고유번호 모으기
    genre_to_indexes = {}
    for i, genre in enumerate(genres):
        genre_to_indexes.setdefault(genre, []).append(i)
        
    # 2. 장르별 총 재생 수 구하기
    genre_to_total = {}
    for genre, idxs in genre_to_indexes.items():
        genre_to_total[genre] = sum(plays[i] for i in idxs)
        
    # 3. 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_to_total.keys(), key=lambda g: genre_to_total[g], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        # 고유 번호 2개까지 재생 수 내림차순, 같으면 번호 오름차순
        sorted_songs = sorted(genre_to_indexes[genre], key=lambda i: (-plays[i], i))
        answer.extend(sorted_songs[:2]) # 최대 2곡까지 수록
    
    return answer