def solution(n):
    answer = ''
    while n > 0:
        nmg = n%3
        n //= 3
        if nmg == 0:
            n -= 1
            nmg = 4
        answer = str(nmg) + answer
    
    return answer