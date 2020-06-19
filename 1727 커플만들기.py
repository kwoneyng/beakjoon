n, m = map(int,input().split())

man = list(map(int,input().split()))
wman = list(map(int,input().split()))

if len(wman)>len(man):
  pick = 0
else:
  pick = 1

people = []

for i in man:
  people.append([i,0])

for i in wman:
  people.append([i,1])

people.sort()
rs = 0
stack = []
queue = []
for i in range(len(people)):
  if people[i][1] == pick:
    queue.append(people[i])
  else: # 선택 받을 때
    stack.append(people[i])
  
  if queue:
    if stack:
      rs += abs(queue.pop(0)[0] - stack.pop()[0])

print(rs)
