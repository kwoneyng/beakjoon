n,m = map(int,input().split())

bd = [int(input()) for i in range(n)]
bd.sort()
left = 0
right = 1
mn = 1e12

while right < n:
    if bd[right] - bd[left] >= m:
        if right > left:
            mn = min(mn, bd[right] - bd[left])
            left += 1
        else:
            right += 1
    else:
        right += 1

print(mn)