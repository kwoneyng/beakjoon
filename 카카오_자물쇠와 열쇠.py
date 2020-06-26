def rotate(key):
    k = len(key)
    rkey = []
    for y in range(k):
        row = []
        for x in range(k-1,-1,-1):
            row.append(key[x][y])
        rkey.append(row)
    return rkey

def expand(key, lock):
    k = len(key)
    l = len(lock)
    s = (k-1)*2 + l
    bd = [[0 for i in range(s)] for i in range(s)]
    for x in range(l):
        for y in range(l):
            bd[x+k-1][y+k-1] =lock[x][y]
    return bd

def solve(key, expand_lock):
    k = len(key)
    el = len(expand_lock)
    for x in range(el-k+1):
        for y in range(el-k+1):
            if match(key, expand_lock, x, y):
                return True
    return False
            
def match(key, expand_lock, x, y):
    k = len(key)
    el = len(expand_lock)
    nexpdl = [i[:] for i in expand_lock]
    for i in range(k):
        for j in range(k):
            if k-1 <= x+i < el-k+1 and k-1 <= y+j < el-k+1:
                nexpdl[x+i][y+j] += key[i][j]
    l = el-(k-1)*2
    for i in range(l):
        for j in range(l):
            if nexpdl[k-1+i][k-1+j] % 2 == 0:
                return False
    return True

def solution(key, lock):
    answer = False
    rotation_key = [key]
    for i in range(3):
        rotation_key.append(rotate(rotation_key[i]))
    expand_lock = expand(key, lock)
    for i in range(4):
        answer = solve(rotation_key[i], expand_lock)
        if answer:
            break  
    return answer