def solution(m, musicinfos):
    for info in musicinfos:
        infos = info.split(',')
        s = infos[0]
        e = infos[1]
        name = infos[2]
        melody = infos[3]
        d = len(melody)
        melody = list(melody)
        q = []
        for j in melody:
            if j == '#':
                q[-1] = q[-1].lower()
                d -= 1
            else:
                q.append(j)
        s = list(map(int,s.split(':')))
        s = s[0]*60 + s[1]
        e = list(map(int,e.split(':')))
        e = e[0]*60 + e[1]
        time = e-s
        total = ''
        r = []
        for i in m:
            if i == '#':
                r[-1] = r[-1].lower()
            else:
                r.append(i)
        m = ''.join(r)
        for i in range(time):
            t = i%d
            total += q[t]
        if m in total:
            return name

m,musicinfos = 	"CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
print(solution(m,musicinfos))