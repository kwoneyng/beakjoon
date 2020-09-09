ss,k = 	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3

def solution(stones, k):
    answer = 0
    l,r = 0, max(stones)
    while l <= r:
        m = (l+r)//2
        stop = 0
        for st in stones:
            if st < m:
                stop += 1
                if stop >= k:
                    r = m-1
                    break
            else:
                stop = 0
        else:
            answer = m
            l = m+1
            
    return answer

print(solution(ss,k))