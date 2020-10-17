from collections import deque
def solution(n, edge):
    answer = 0
    nxtArr = [[] for i in range(n+1)]
    for a,b in edge:
        nxtArr[a].append(b)
        nxtArr[b].append(a)
    vis = [0]*(n+1)
    q = deque()
    q.append(1)
    vis[1] = 1
    while q:
        for i in range(len(q)):
            cur = q.popleft()
            for nxt in nxtArr[cur]:
                if vis[nxt] == 0:
                    q.append(nxt)
                    vis[nxt] = 1
        if q:
            answer = len(q)
    
    return answer

n,e =	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,e))