from collections import deque
from heapq import heappop, heappush
n, m = map(int,input().split())
nxtArr = [[] for i in range(n+1)]
indegree = [0] * (n+1)
for i in range(m):
    pre, post = map(int,input().split())
    nxtArr[pre].append(post)
    indegree[post] += 1

q = []
for i in range(1,n+1):
    if indegree[i] == 0:
        heappush(q,i)

while q:
    cur = heappop(q)
    print(cur, end=' ')
    for i in nxtArr[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(q,i)