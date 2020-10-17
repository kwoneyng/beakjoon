def one(word):
    if word == '':
        return ''
    else:
        u,v = two(word)
        rs = three(u,v)
        return rs

def two(w):
    cnt = 0
    for i,c in enumerate(w):
        if c == '(':
            cnt += 1
        else :
            cnt -= 1
        if cnt == 0:
            return w[:i+1], w[i+1:]
            
def three(u,v):
        nxt = True
        cnt = 0
        for i in u:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                nxt = False
        if nxt:
            return u + one(v)
        else:
            rs = '('
            rs += one(v)
            rs += ')'
            u = u[1:-1]
            for i in u:
                if i == '(':
                    rs += ')'
                else:
                    rs += '('
            return rs
        
def solution(p):
    answer = ''
    answer = one(p)
    return answer

p = "(()())()"
print(solution(p))