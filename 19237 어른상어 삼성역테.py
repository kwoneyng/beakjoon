near = [[1,0],[-1,0],[0,-1],[0,1]]
n,m,k = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]

def nor(x):
  return int(x)-1

start = list(map(nor,input().split()))

di = {}
for i in range(1,m+1):
  di[i] = []
  for j in range(4):
    di[i].append(list(map(nor,input().split())))

shark = {}

for i in range(n):
  for j in range(n):
    cur = bd[i][j]
    if cur != 0:
      shark[cur] = [i,j,start[cur-1]]

vis = [[0]*n for i in range(n)]
for key, val in shark.items():
  x,y,p = val
  vis[x][y] = [key,k]

for i in vis:
  print(i)

for i in range(1,m+1):
  if shark.get(i):
    x,y,p = shark[i]
    bd[x][y] = 0
    back = 0
    for j in di[i][p]:
      a,b = near[j]
      xi,yi = x+a,y+b
      if 0<=xi<n and 0<=yi<n:
        if vis[xi][yi] == 0:
          if bd[xi][yi] == 0:
            bd[xi][yi] = i
            vis[xi][yi] = [i,k]
          break
        elif vis[xi][yi][0] == i:
          back = [xi,yi]
    elif back != 0:
      x,y = back
      bd[x][y] = i
      vis[x][y] = [i,k]


