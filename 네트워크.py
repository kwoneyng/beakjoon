
global near
near = [[-1,0],[0,1],[1,0],[0,-1]]
def dfs(x, y, computers, vis):
    n = len(computers)
    vis[x][y] = 1
    for a,b in near:
        xi,yi = x+a, y+b
        if 0<=xi<n and 0<=yi<n and computers[xi][yi] == 1:
            if vis[xi][yi] == 0:
                dfs(xi,yi,computers,vis)
    

def solution(n, computers):
    answer = 0
    vis = [[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            if computers[x][y] == 1 and vis[x][y] == 0:
                answer += 1
                dfs(x,y,computers,vis)
    
    return answer

n, computers = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n,computers)