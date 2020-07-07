n = int(input())

dp = [0]*1000001
for i in range(11):
    dp[i] = i

dp[11] = 20

cur = 11
flag = 1
while flag:
    flag = 0
    pre = dp[cur]
    if pre == -1:
        dp[cur+1] = 0
        cur += 1
        break
    stpr = str(pre)
    len_stpr = len(stpr)
    pre = list(map(int,(list(stpr))))
    for i in range(len_stpr-1,0,-1):
        if pre[i]+1 >= pre[i-1]:
            if i-1 == 0:
                if pre[0] == 9:
                    len_stpr+=1
                    if len_stpr > 10:
                        dp[cur+1] = 0
                        break
                    nxt = ''
                    for k in range(len_stpr):
                        nxt = str(k) + nxt
                    dp[cur+1] = int(nxt)
                    flag = 1
                    cur += 1
                    break
                else:
                    pre[0] += 1
                    for i in range(len(pre)-1,0,-1):
                        pre[i] = len(pre)-i-1
                    nxt = ''
                    for k in pre:
                        nxt += str(k)
                    dp[cur+1] = int(nxt)
                    flag = 1
                    cur += 1
                    break
            else:
                pass
        else:
            pre[i] += 1
            nxt = ''
            for j in range(len(pre)-1,i,-1):
                pre[j] = len(pre)-j-1
            for k in pre:
                nxt += str(k)
            dp[cur+1] = int(nxt)
            flag = 1
            cur += 1
            break
    if cur == n+1:
        break

# print(dp[:n+1])

if dp[n]:
    print(dp[n])
elif n==0:
    print(0)
else:
    print(-1)