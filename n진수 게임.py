def solution(n, t, m, p):
    answer = ''
    rs = '0'
    over = ['A','B','C','D','E','F']
    for i in range(m*t):
        a = i
        cur = ''
        while a > 0:
            new = a%n
            if new >= 10:
                new = over[new%10]
                cur = new + cur
            else:
                cur = str(new) +cur
            a //= n
        rs += cur
    for i in range(t):
        answer += rs[i*m+p-1]
    return answer

n,t,m,p = 16, 16, 2, 1
print(solution(n,t,m,p))