n = int(input())
board = [list(map(int,input().split())) for i in range(n)]
blue = 0
white = 0


def check(board, n, first):
    global blue, white
    for x in range(n):
        for y in range(n):
            if board[x][y] != first:
                cutting(board, n)
                return
    if first == 0:
        white += 1
    else:
        blue += 1
    return

def cutting(board,n):
    half = n//2
    c_board = [[],[],[],[]]
    
    for x in range(half):
        c_board[0].append(board[x][:half])
        c_board[1].append(board[x][half:])
    for x in range(half,n):
        c_board[2].append(board[x][:half])
        c_board[3].append(board[x][half:])
    
    for i in c_board:
        check(i, half, i[0][0])


check(board,n,board[0][0])
print(white)
print(blue)
    