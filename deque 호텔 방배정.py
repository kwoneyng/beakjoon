k,rn = 	10, [1, 3, 4, 1, 3, 1]

from collections import deque

def solution(k, room_number):
    answer = []
    ht = {}
    stack = deque()
    for n in room_number:
        t = n
        while ht.get(t):
            stack.append(t)
            t = ht.get(t)+1
        while stack:
            s = stack.pop()
            ht[s] = t
        ht[t] = t
        answer.append(ht[n])
    return answer

print(solution(k,rn))