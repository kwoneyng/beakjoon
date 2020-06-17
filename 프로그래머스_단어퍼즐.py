# strs, t = ["ab", "na", "n", "a", "bn"], "nabnabn"
# strs, t =	["ba", "na", "n", "a"], "banana"
strs, t =	["app", "ap", "p", "l", "e", "ple", "pp"], "apple"
# strs, t = ["ba", "an", "nan", "ban", "n"], "banana"

n = len(t)
dp = [1e9]*(n+1)
dp[0] = 0
for i in range(n):
  chk = t[i]
  for st in strs:
    m = len(st)
    if chk == st[-1]:
      if st == t[i-m+1:i+1]:
        dp[i+1] = min(dp[i-m+1] + 1, dp[i+1])

print(dp)