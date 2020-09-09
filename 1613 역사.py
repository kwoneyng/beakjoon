    import sys
    input = sys.stdin.readline

    n,k = map(int,input().split())
    bd = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,input().split())
        bd[a][b] = -1
        bd[b][a] = 1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if bd[i][k] and bd[i][k] == bd[k][j]:
                    bd[i][j] = bd[i][k]
                    bd[j][i] = -bd[i][k]

    for _ in range(int(input())):
        a,b = map(int,input().split())
        print(bd[a][b])
