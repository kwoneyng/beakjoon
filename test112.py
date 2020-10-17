from collections import deque

n,m = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]
near = [[-1,0],[0,1],[1,0],[0,-1]]
vis = [[0]*m for i in range(n)]
ans = 0

queue = deque()

queue.append([0,0])
ans = 0
while queue:
    x,y = queue.popleft()
    if x == n-1 and y == m-1:
        ans += 1
    for a,b in near:
        xi,yi = a+x,b+y
        if 0<=xi<n and 0<=yi<m and bd[x][y] > bd[xi][yi]:
            if vis[xi][yi] == 0:
                vis[xi][yi] = 1
                queue.append([xi,yi])
            else:
                ans += 1

print(ans)