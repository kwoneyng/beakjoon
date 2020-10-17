from collections import deque
def solution(n, path, order):
    vis = [0] * n
    indegree = [0]*n
    nxtArr = [[] for i in range(n)]
    for a,b in path:
        nxtArr[a].append(b)
        nxtArr[b].append(a)
    q = deque([0])
    tree = {}
    tree[0] = []
    vis[0] = 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if tree.get(cur) != None:
                for nxt in nxtArr[cur]:
                    if vis[nxt] == 0:
                        vis[nxt] = 1
                        q.append(nxt)
                        tree[nxt] = []
                        tree[cur].append(nxt)
    for a,b in order:
        tree[a].append(b)

    for i in tree.keys():
        for node in tree[i]:
            indegree[node] += 1
    
    q = deque([0])
    vis = [0]*n
    while q:
        cur = q.popleft()
        vis[cur] = 1
        for nxt in tree[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
            elif indegree[nxt] < 0:
                return False
    if vis.count(0):
        return False
    else:
        return True



n,p,o = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]
print(solution(n,p,o))