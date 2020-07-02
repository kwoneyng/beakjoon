n = int(input())
arr = [int(input()) for i in range(n)]

# chage = 0

# for i in range(n):
#   chage = 0
#   for j in range(n-i-1):
#     if arr[j] > arr[j+1]:
#       chage = 1
#       arr[j], arr[j+1] = arr[j+1], arr[j]
#   if chage == 0:
#     print(i+1)
#     break

earr = list(enumerate(arr))
earr.sort(key = lambda x: x[1])
# print(earr)
rs = 0
for i in range(n):
    if earr[i][0] > i:
        rs = max(rs, earr[i][0]-i)

print(rs+1)