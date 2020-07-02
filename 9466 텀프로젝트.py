# 싸이클이 만들어 질 경우에만 팀이 생성된다.

def cycle(adj_list, n, x):
    global cyles
    path = [x]
    q = [x]
    while q:
        cur = q.pop()
        vis[cur] = 1
        nxt = adj_list[cur]
        if vis[nxt] != 0:
            if nxt in path:
                start = path.index(nxt)
                path = path[start:]
                cyles += path
            return
        else:
            path.append(nxt)
            q.append(nxt)


for t in range(int(input())):
    n = int(input())
    adj_list = [0 for i in range(n+1)]
    data = list(map(int,input().split()))
    vis = [0]*(n+1)
    cyles = []
    for i in range(n):
        adj_list[i+1]=data[i]
    for i in range(n):
        if vis[i+1] == 0:
            cycle(adj_list,n,i+1)
    print(n - len(cyles))



# 다른풀이
# import sys
# input = sys.stdin.readline

# for T in range(int(input())):
#     n = int(input())
#     next = [0]+[*map(int,input().split())]
#     indegree = [0]*(n+1)
#     for i in next:
#         indegree[i] += 1

#     q = [i for i in range(1,n+1) if indegree[i] == 0]
#     ans = 0
    
#     while q:
#         cur = q.pop()
#         ans += 1
#         indegree[next[cur]] -= 1
#         if indegree[next[cur]] == 0:
#             q.append(next[cur])
#     print(ans)