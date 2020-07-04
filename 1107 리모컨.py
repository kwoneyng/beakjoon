target = int(input())
n = int(input())
if n > 0:
    disable = list(input().split())
else:
    disable = []
mn = 1e9
for i in range(1000001):
    for j in disable:
        if j in str(i):
            break
    else:
        mn = min(mn, abs(target-i)+len(str(i)))
only = abs(target-100)

mn = min(only, mn)
print(mn)
