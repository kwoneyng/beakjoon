from heapq import heappop,heappush
import sys
input = sys.stdin.readl

n = int(input())
m = int(input())

nxtarr = [[] for _ in range(n+1)]

INF = sys.maxsize
rs = [[INF,''] for i in range(n+1)]

for _ in range(m):
    s,e,v = map(int, input().split())
    nxtarr[s].append([v,e])

S,E = map(int,input().split())
rs[S][0] = 0
rs[S][1] = str(S)

q = []
heappush(q,[0,S])
while q:
    val, node = heappop(q)

    if rs[node][0] < val:
        continue

    for nval, nxt in nxtarr[node]:
        nval += val
        if nval < rs[nxt][0]:
            rs[nxt][0] = nval
            rs[nxt][1] = rs[node][1] + ',' + str(nxt)
            heappush(q,[nval, nxt])

print(rs[E][0])
trace = rs[E][1].split(',')
print(len(trace))
print(*trace)
