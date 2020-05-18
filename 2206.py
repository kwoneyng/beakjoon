from collections import deque

n,m = map(int,input().split())
bd = [list(map(int,list(input()))) for i in range(n)]
vis = [[[1e9]*2 for i in range(m)] for i in range(n)]
q=deque([[0,0,1,1]])
near = [[-1,0],[0,1],[1,0],[0,-1]]
vis[0][0][0] = 1
while q:
    x,y,des,cost = q.popleft()
    for a,b in near:
        xi,yi = a+x, b+y
        if 0<=xi<n and 0<=yi<m:
            if bd[xi][yi] == 1:
                if des == 1 and vis[xi][yi][0] > cost+1:
                    vis[xi][yi][0] = cost+1
                    q.append([xi,yi,0,cost+1])
            else:
                if vis[xi][yi][des] > cost+1:
                    vis[xi][yi][des] = cost+1
                    q.append([xi,yi,des,cost+1])


res = 0
if vis[n-1][m-1][0] == 1e9 and vis[n-1][m-1] == 1e9:
    res = -1
else:
    res = min(vis[n-1][m-1][0], vis[n-1][m-1][1])

print(res)