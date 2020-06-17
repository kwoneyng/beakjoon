# strs, t = ["ab", "na", "n", "a", "bn"], "nabnabn"
# strs, t =	["ba", "na", "n", "a"], "banana"
strs, t =	["app", "ap", "p", "l", "e", "ple", "pp"], "apple"
# strs, t = ["ba", "an", "nan", "ban", "n"], "banana"

n = len(t)
dp = [1e9]*(n+1)
dp[0] = 0
for i in range(n):
  for k in range(1,6):
    if i+k <= n and t[i:i+k] in strs:
      dp[i+k] = min(dp[i]+1,dp[i+k] )
print(dp)


# def solution(strs, t):
#     dp = {}
#     for i in range(len(t)):
#         dp[i] = float('inf')

#     for i in range(len(t)-1, -1, -1):
#         for k in range(1,6):
#             if t[i:i+k] in strs:
#                 dp[i] = min(dp.get(i), dp.get(i+k, 0)+1)
#     return dp.get(0) if dp.get(0) != float('inf') else -1