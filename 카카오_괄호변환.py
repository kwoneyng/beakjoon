ecd = {'(':1, ')':-1}
rvs = {'(':')', ')':'('}

def divid(p):
    global ecd, rvs
    if len(p) == 0:
        return ''
    val = 0
    for i in range(len(p)):
        val += ecd[p[i]]
        if val == 0:
            u, v = p[:i+1], p[i+1:]
            break
    if u[0] == '(':
        # 3번
        vr = divid(v)
        return u + vr
        pass
    else:
        # 4번
        ans = '('
        vr = divid(v)
        ans += vr
        ans += ')'
        for i in u[1:-1]:
            ans += rvs[i]
        return ans
        pass
    
    
    
def solution(p):
    answer = ''
    answer = divid(p)
    return answer