def solution(w,h):
    answer = 0
    if w < h:
        w,h = h,w
    degree = w/h
    start = 0
    for i in range(1,1+h):
        end = degree*i
        answer += (int(end)+1 - int(start))
        start = end
    return w*h - answer

w,h=499, 1000
print(solution(w,h))