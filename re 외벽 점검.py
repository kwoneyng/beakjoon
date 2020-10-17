n,w,d =	200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]

def solution(n, weak, dist):
    answer = 9
    totalSet = []
    dist.sort(reverse=True)
    l = len(weak)
    for _ in range(l):
        item = weak[_:] + weak[:_]
        totalSet.append(item)
    for item in totalSet:
        for idx,j in enumerate(dist):
            start = item[0]
            while item and j >0:
                nxt = item[0]
                if nxt >= start:
                    d = nxt - start
                else:
                    d = n + nxt - start
                if j - d >= 0:
                    j -= d
                    start = item.pop(0)
                else:
                    break
            if not item:
                answer = min(answer, idx)
                break
        
    if answer < 9:
        return answer+1
    else:
        return -1

print(solution(n,w,d))