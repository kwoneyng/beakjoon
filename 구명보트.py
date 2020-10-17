def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    l,r = 0,n-1
    while True:
        if l > r:
            break
        else:
            answer += 1
        if people[l] + people[r] <= limit:
            r -= 1
            l += 1
        else:
            r -= 1
        
    return answer

people, limit = [70, 50, 80, 50], 100
print(solution(people,limit))