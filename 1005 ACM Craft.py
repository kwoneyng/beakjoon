from collections import deque
for t in range(int(input())):
    answer = 0
    N,K = map(int,input().split())
    vis = [0]*(N+1)
    arr = [0] + list(map(int,input().split()))
    nxtArr = [[] for i in range(N+1)]
    for _ in range(K):
        c,n = map(int,input().split())
        nxtArr[n].append(c)
    win = int(input())
    q = deque()
    q.append(win)
    while q:
        cur = q.popleft()
        for nxt in nxtArr[cur]:
            vis[nxt] += 1
            q.append(nxt)

    q.append(win)
    while q:
        maxTime = 0
        viscnt = []
        for _ in range(len(q)):
            cur = q.popleft()
            if vis[cur] == 0:
                maxTime = max(arr[cur], maxTime)
            for nxt in nxtArr[cur]:
                viscnt.append(nxt)
                q.append(nxt)
        for i in viscnt:
            vis[i] -= 1
        answer += maxTime
    print(answer)