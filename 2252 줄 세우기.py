from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

nxtArr =[[] for i in range(n+1)]
tall = [0]*(n+1)
small = [0]*(n+1)

for _ in range(m):
    t,s = map(int,input().split())
    nxtArr[t].append(s)
    tall[s] += 1
    small[t] += 1


q = deque()
for i in range(1,n+1):
    if tall[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end=' ')
    for nxt in nxtArr[cur]:
        tall[nxt] -= 1
        if tall[nxt] == 0:
            q.append(nxt)            

