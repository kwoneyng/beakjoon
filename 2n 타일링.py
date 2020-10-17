def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    answer = 0
    l = 1
    r = 2
    for _ in range(n-3):
        answer = (l+r)
        l,r = r, answer
    return answer

n = 14
print(solution(n))