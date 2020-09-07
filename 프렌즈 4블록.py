def find(b,t,x,y):
    for i in range(2):
        for j in range(2):
            if b[x+i][y+j] != t:
                return False
    return True

def solution(m, n, board):
    answer = 0
    start = 1
    roboard = [[] for i in range(n)]
    for i in range(m):
        for j in range(n):
            roboard[j].append(board[i][j])
    board = roboard

    while start:
        ht = {}
        for x in range(n):
            for y in range(m):
                if 0<=x+1< n and 0<=y+1<m and board[x][y].isalpha():
                    target = board[x][y]
                    if find(board,target,x,y):
                        for i in range(2):
                            for j in range(2):
                                ht[(x+i, y+j)] = 1
        if not ht:
            start = 0
        else:
            for xy, val in ht.items():
                x,y = xy
                answer += val
                board[x][y] = '0'
            for i in range(n):
                cnt = board[i].count('0')
                board[i] = ''.join(board[i]).replace('0','')
                for _ in range(cnt):
                    board[i] = '0'+board[i]
                board[i] = list(board[i])
    return answer

m,n,b =	6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,b))