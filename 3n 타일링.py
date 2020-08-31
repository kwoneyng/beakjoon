def solution(n):
    dp = [0] * (n+1)
    dp[2] = 3
    for i in range(4,n+1,2):
        dp[i] = dp[i-2] * 3
        for j in range(4,n+1,2):
            dp[i] += dp[i-j] * 2
    return dp[n] % 1000000007

n = int(input())
print(solution(n))

dp = [0]*(n+1)
dp[0] = 1
special = 0
for i in range(2,n+1,2):
    dp[i] = dp[i-2]*3 + special*2
    special += dp[i-2]
