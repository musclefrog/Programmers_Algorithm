def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    cities = [city.lower() for city in cities] # '대소문자 구분을 하지 않는다'고 했으므로 모두 소문자화
    
    for city in cities:
        if city in cache: # cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # cache miss
            if len(cache) == cacheSize and cacheSize > 0: # '범위는 0 <= cacheSize <= 30 이다'라고 했으므로 0보다 큰지 확인해줘야함
                cache.pop(0) # 인덱스를 지정해서 pop 할 수도 있음
            if cacheSize > 0:
                cache.append(city)
            answer += 5
    return answer