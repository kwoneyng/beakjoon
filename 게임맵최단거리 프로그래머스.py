def solution(maps):
    near = [[-1,0],[0,1],[1,0],[0,-1]]
    n = len(maps)
    m = len(maps[0])
    answer = 1
    q = []
    q.append([0,0])
    maps[0][0] = 0
    while q:
        answer += 1
        for i in range(len(q)):
            x,y = q.pop(0)
            for a,b in near:
                xi,yi = x+a, y+b
                if 0<=xi<n and 0<=yi<m and maps[xi][yi]:
                    if xi == n-1 and yi == m-1:
                        return answer
                    q.append([xi,yi])
                    maps[xi][yi] = 0
    return -1