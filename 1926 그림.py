n,m = map(int,input().split())
board = [list(map(int,input().split())) for i in range(n)]
near = [[-1,0],[0,1],[1,0],[0,-1]]
cnt = 0
max_c = 0
vis = [[0]*m for i in range(n)]
def find(x,y):
    global max_c
    q=[[x,y]]
    c = 0
    while q:
        x,y = q.pop()
        c += 1
        for a,b in near:
            xi,yi = x+a, y+b
            if 0<=xi<n and 0<=yi<m and board[xi][yi] == 1 and vis[xi][yi]==0:
                vis[xi][yi] = 1
                q.append([xi,yi])
    max_c = max(max_c, c)


for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and vis[i][j] == 0:
            cnt += 1
            vis[i][j] = 1
            find(i,j)
print(cnt)
print(max_c)
            