def solution(cookie):
    answer = 0
    n = len(cookie)
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == j:
                dp[i][i] = cookie[i]
            else:
                dp[i][j] = dp[i][j-1]+cookie[j]
    
    for l in range(n//2):
        for r in range(l+2,n):
            for m in range(l+1,r):
                if dp[l][m] == dp[m+1][r]:
                    answer = min(dp[l][m], answer)
    
    return answer

cookie = [1,1,2,3]
print(solution(cookie))
