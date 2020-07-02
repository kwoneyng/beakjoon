n,m = map(int,input().split())
sht = list(map(int,input().split()))
lng = list(map(int,input().split()))

if n > m:
  n,m = m,n
  sht, lng = lng, sht

sht.sort()
lng.sort()

score = [[0]*n for i in range(m)]
for x in range(m):
  for y in range(n):
    score[x][y] = abs(lng[x]-sht[y])

dp = [[0]*n for i in range(m)]
for x in range(m):
  dp[x][0] = score[x][0]

for i in score:
  print(i)

for y in range(1,n):
  for x in range(m):
    dp[x][y] = dp

