def solution(n, times):
    answer=999999999999999999999999999999
    l,r = min(times)*n//len(times),max(times)*n//len(times)+1
    while l < r:
        cnt = 0
        m = (l+r)//2
        for time in times:
            cnt += m//time
        if cnt > n:
            r = m
        elif cnt < n:
            l = m+1
        else:
            answer = min(answer,m)
            r -=1
    return answer


n,t=6, [7, 10]
print(solution(n,t))