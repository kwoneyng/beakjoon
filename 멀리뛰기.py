def solution(n):
    if n < 2:
        return n
    answer = 0
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(1,n-1):
        dp[i+1] = dp[i-1]+ dp[i]

    return dp[n-1]%1234567