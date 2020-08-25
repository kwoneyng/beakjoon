def solution(n, results):
    total = [[0]*n for i in range(n)]
    for a,b in results:
        a -= 1
        b -= 1
        total[a][b] = 1
        total[b][a] = -1
    for x in range(n):
        for y in range(n):
            for k in range(n):
                if total[x][k] != 0 and total[x][k] == total[k][y]:
                    total[x][y] = total[x][k]
    answer = 0
    for i in total:
        print(i)
        if i.count(0) == 1:
            answer += 1
    return answer

n, results = 8, [[1, 2], [2, 3], [3, 4], [4,5], [5, 6], [6, 7], [7, 8]] 
print(solution(n,results))