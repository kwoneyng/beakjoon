import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

arr.sort(key=lambda x: [x[0],x[1]])
room = [arr.pop(0)[1]]

for s,e in arr:
  if room[0] <= s:
    heappop(room)
    heappush(room,e)
  else :
    heappush(room,e)

print(len(room))