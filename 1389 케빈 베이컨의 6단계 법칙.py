n,m = map(int,input().split())

board = [[10001]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1

for i in range(n):
    board[i][i] = 0
minny = 10001
for k in range(n):
    for x in range(n):
        for y in range(n):
            if board[x][k] <10000 and board[k][y] < 10000:
                board[x][y] = min(board[x][y], board[x][k]+board[k][y])

answer = 0
for i,b in enumerate(board):
    if minny > sum(b):
        answer = i+1
        minny = sum(b)
print(answer)
