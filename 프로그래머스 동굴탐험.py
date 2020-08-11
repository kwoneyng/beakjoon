def solution(n, path, order):
    answer = False
    vis = [0]*n
    vis[0] = 1
    nxt_ls = [[] for i in range(n)]
    ord_ls = [0 for i in range(n)]
    rel_ls = [0 for i in range(n)]
    for a,b in path:
        nxt_ls[a].append(b)
        nxt_ls[b].append(a)
    for a,b in order:
        ord_ls[b] = a
        rel_ls[a] = b
    q = [0]
    while q:
        node = q.pop(0)
        if vis[ord_ls[node]]:
            vis[node] = 1
            if len(nxt_ls[node]) > 1 or node == 0:
                for i in nxt_ls[node]:
                    if vis[i] == 0:
                        q.append(i)
            mod = rel_ls[node]
            if mod and vis[mod] == -1:
                q.append(mod)
        else:
            vis[node] = -1
    if vis.count(0) + vis.count(-1):
        answer = False
    else:
        answer = True
    
    return answer

n, path, order = 	9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]

print(solution(n,path,order))