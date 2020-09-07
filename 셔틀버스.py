def wtii(string):
    string = list(map(int,string.split(':')))
    hour = int(string[0])*60
    minute = int(string[1])
    return hour+minute

def rt(a):
    hour = a//60
    minute = a%60
    hour = str(hour)
    minute = str(minute)
    for i in range(2-len(hour)):
        hour = '0'+hour
    for i in range(2-len(minute)):
        minute = '0'+minute
    return hour +':'+minute

def solution(n, t, m, timetable):
    timetable = list(map(wtii,timetable))
    timetable.sort(reverse=True)
    start = 9*60
    for _ in range(n):
        bus = []
        for _ in range(m):
            if timetable:
                if timetable[-1] <= start:
                    bus.append(timetable.pop())
        start += t
    start -= t
    if len(bus) == m:
        return rt(bus[-1]-1)
    else:
        return rt(start)

n,t,m,tt = 2, 10, 2, ["09:10", "09:09", "08:00"]
print(solution(n,t,m,tt))