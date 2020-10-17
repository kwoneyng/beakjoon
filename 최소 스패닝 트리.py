from heapq import heappop, heappush
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
nxtarr = [[]for i in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    nxtarr[a].append([c,b])
    nxtarr[b].append([c,a])

cost = [99999999999999]*(v+1)
cost[0] = 0
cost[1] = 0

vis = [0]*(v+1)
vis[0] = 1

q = []
heappush(q,[0,1])

while q:
    val, node = heappop(q)
    if vis[node]:
        continue
    vis[node] = 1
    for nval, nxt in nxtarr[node]:
        if cost[nxt] < nval:
            continue
        if vis[nxt]:
            continue
        heappush(q,[nval,nxt])
        cost[nxt] = nval
print(sum(cost))
