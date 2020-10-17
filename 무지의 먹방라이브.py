from collections import deque
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food_times = list(enumerate(food_times))
    food_times.sort(key=lambda x:x[1])
    food_times = deque(food_times)
    start = 0
    while k > 0 and food_times:
        n = len(food_times)
        idx, cur = food_times[0]    
        if k > n*(cur-start):
            k -= n*(cur-start)
            food_times.popleft()
            start = cur
        else:
            cut = k%len(food_times)
            food_times = list(food_times)
            food_times.sort()
            return food_times[cut][0]+1
            
    return 0