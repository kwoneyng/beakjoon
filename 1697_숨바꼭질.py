n,m = map(int,input().split())

vis = [0]*1000001

q = [n]
cnt = 0
while q:
    if n == m:
        break
    cnt += 1
    for i in range(len(q)):
        nn = q.pop(0)
        if nn-1 >= 0 and vis[nn-1] == 0:
            q.append(nn-1)
            vis[nn-1] = 1
        if nn*2 <= 100000 and vis[nn*2] == 0:
            q.append(nn*2)
            vis[nn*2] = 1
        if nn+1 <= 100000 and vis[nn+1] == 0:
            q.append(nn+1)
            vis[nn+1] = 1
    if vis[m] == 1:
        break

print(cnt)