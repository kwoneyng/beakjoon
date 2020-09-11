money =	[1, 2, 3, 1]

def solution(money):
    answer = 0
    n = len(money)
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[1],dp[0])
    for i in range(2,n-1):
        dp[i] = max(dp[i-1],dp[i-2] + money[i])
    answer = max(dp)
    dp = [0]*n
    dp[1] = money[1]
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = max(max(dp),answer)
    
    return answer

print(solution(money))