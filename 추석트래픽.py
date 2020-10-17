def solution(lines):
    answer = 0
    data = []
    for line in lines:
        line = line.split()
        start = line[1].replace('.',':').split(':')
        end = line[2].replace('s','')
        start = float(start[0])*3600000 + float(start[1])*60000 + float(start[2])*1000 + float(start[3])
        end = start - float(end)*1000 + 1
        data.append([start,end])

    n = len(data)
    for i in range(n):
        st, ed = data[i]
        stsc, edsc = 0,0
        for j in range(i, n):
            nst, ned = data[j]
            if st <= nst < st+1000 or st <= ned < st+100 or (st > nst and st+1000 < ned):
                stsc += 1
            if ed <= nst < ed+1000 or ed <= ned < ed+1000 or (ed > nst and ed+1000 < ned ):
                edsc += 1
        answer = max(answer, stsc, edsc)
    return answer

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))