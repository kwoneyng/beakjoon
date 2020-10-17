def solution(cacheSize, cities):
    answer = 0
    ht = {}
    cache = []
    for city in cities:
        city = city.upper()
        if ht.get(city):
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
                ht[city] = 1
            elif cache:
                del ht[cache.pop(0)]
                ht[city] = 1
                cache.append(city)
    return answer

cacheSize, cities = 3, ['Jeju', 'Pangyo', 'Seoul', 'assa','Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
print(solution(cacheSize, cities))