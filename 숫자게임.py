def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    start = 0
    n = len(B)
    for i in A:
        while start < n:
            if i < B[start]:
                answer += 1
                start += 1
                break
            else:
                start += 1
            
    return answer

A,B = 	[5, 1, 3, 7], [2, 2, 6, 8]
print(solution(A,B))