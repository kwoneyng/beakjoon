def solution(n, stations, w):
    stations = [-w] + stations + [n+w+1]
    nmg = []
    for i in range(len(stations) -1):
        nmg.append(stations[i+1]-stations[i]-2*w-1)

    cnt = 0
    for j in nmg:
        if j > 0:
            if j % (2*w+1) > 0:
                cnt+=1
            cnt += j//(2*w+1)


    return cnt

n,s,w = 20,[5,9,16],1
print(solution(n,s,w))