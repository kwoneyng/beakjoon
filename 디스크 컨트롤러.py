from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    t = 0
    ht = {}
    h = []
    new = 0
    for s,time in jobs:
        if not ht.get(s):
            ht[s] = [time]
        else:
            ht[s].append(time)
    while t < 1000:
        if ht.get(t):
            for i in ht[t]:
                heappush(h,[i,t])
        if new <= t:
            if h:
                nxt, start = heappop(h)
                new += nxt
                answer += new - start
            else :
                new += 1
        t += 1

    return answer//len(jobs)




# jobs = [[0, 3], [1, 9], [2, 6]]
# jobs = [[0, 3], [4, 3], [8, 3]] # 3
# jobs = [[0, 5], [6, 1], [6, 2]] # 3
# jobs = [[0, 5], [6, 2], [6, 1]] # 3
# jobs = [[0, 5], [2, 2], [5, 3]] # 5
jobs = [[0, 10], [4, 10], [5, 11], [40, 2]] # 15
# jobs = [[0, 5], [1, 2], [5, 5]] # 6
# jobs = [[0, 3], [1, 9], [500, 6]] # 6
# jobs = [[0, 6], [0, 8], [7, 1]]
print(solution(jobs))