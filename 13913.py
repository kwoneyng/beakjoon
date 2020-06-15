from collections import deque
n,m = map(int,input().split())

q = deque([[str(n),n,1]])
vis = [0]*100002
vis[n] = 1
if n != m:
  while q:
    path, nd, cnt = q.popleft()
    if nd + 1 < 100001:
      if nd + 1 == m:
        print(cnt)
        print(path +f' {nd+1}')
        break
      elif vis[nd+1] == 0:
        q.append([path + f' {nd+1}',nd+1,cnt+1])
        vis[nd+1] = 1
    if nd - 1 >= 0:
      if nd - 1 == m:
        print(cnt)
        print(path +f' {nd-1}')
        break
      elif vis[nd-1] == 0:
        q.append([path + f' {nd-1}',nd-1,cnt+1])
        vis[nd-1] = 1
    if nd*2 < 100001:
      if nd*2 == m:
        print(cnt)
        print(path +f' {nd*2}')
        break
      elif vis[nd*2] == 0:
        q.append([path + f' {nd*2}',nd*2,cnt+1])
        vis[nd*2] = 1
else:
  print(0)
  print(n)