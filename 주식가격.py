def solution(prices):
    n = len(prices)
    answer = [0]*n
    time = 0
    stack = []
    while time < n:
        while stack:
            if stack[-1][0] > prices[time]:
                _,t = stack.pop()
                answer[t] = time - t
            else: break
        stack.append([prices[time],time])
        time += 1
    while stack:
        _, t = stack.pop()
        answer[t] = n-1 - t
    return answer

p = [1, 2, 3, 2, 3]	
print(solution(p))