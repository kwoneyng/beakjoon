from collections import deque

n,m = map(int,input().split())
bd = [list(map(int,input())) for i in range(n)]
near = [[0,1],[1,0],[-1,0],[0,-1]]
q = deque()
q.append([0,0,1])
vis = [[0]*m for i in range(n)]

while q:
	x,y,cnt = q.popleft()
	if x == n-1 and y == m-1:
		print(cnt)
		break
	for a,b in near:
		xi,yi = a+x,b+y
		if 0<=xi<n and 0<=yi<m and bd[xi][yi] == 1 and vis[xi][yi] == 0:
			vis[xi][yi] = 1
			q.append([xi,yi,cnt+1])