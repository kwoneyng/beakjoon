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

    for i in total:
        print(i)

n, results = 5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n,results)