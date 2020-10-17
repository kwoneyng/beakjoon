from collections import deque

n,m,e = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
sx,sy = map(lambda x: int(x)-1,input().split())
cus_ht = {}
for i in range(m):
    cx,cy,ex,ey = map(lambda x: int(x)-1,input().split())
    cus_ht[(cx,cy)] = (ex,ey)
near = [[-1,0],[0,-1],[0,1],[1,0]]

def target(sx,sy,arr,cus_ht):
    vis = [[0]*n for i in range(n)]
    vis[sx][sy] = 1
    if cus_ht.get((sx,sy)):
        return (sx,sy), 0
    q = deque([(sx,sy)])
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            x,y = q.popleft()
            for a,b in near:
                xi,yi = a+x,b+y
                if 0<=xi<n and 0<=yi<n:
                    if cus_ht.get((xi,yi)):
                        return (xi,yi), cnt
                    elif vis[xi][yi] == 0 and arr[xi][yi] == 0:
                        vis[xi][yi] = 1
                        q.append((xi,yi))
    return -1,-1

def go(s,e,arr):
    vis = [[0]*n for i in range(n)]
    q = deque([s])
    cnt = 0
    while q:
        cnt+=1
        for _ in range(len(q)):
            x,y = q.popleft()
            for a,b in near:
                xi,yi = a+x,b+y
                if 0<=xi<n and 0<=yi<n:
                    if (xi,yi) == e:
                        return cnt
                    elif vis[xi][yi] == 0 and arr[xi][yi] == 0:
                        vis[xi][yi] = 1
                        q.append((xi,yi))
    return -1

answer = 0
for i in range(m):
    t,use = target(sx,sy,arr,cus_ht)
    if t != -1 and e-use >= 0:
        e-=use
        end = cus_ht[t]
        del cus_ht[t]
        use = go(t,end,arr)
        if use != -1 and e-use >= 0:
            sx,sy = end
            e += use
        else:
            answer = -1
            break
    else:
        answer = -1
        break
if answer == -1:
    print(answer)
else:
    print(e)

