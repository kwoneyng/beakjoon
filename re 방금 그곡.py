def parse(a):
    return a.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    answer = ''
    ht = {}
    m = parse(m)
    catch = [0,'']
    for info in musicinfos:
        st,ed,nm,melody = info.split(',')
        st = list(map(int,st.split(':')))
        ed = list(map(int,ed.split(':')))
        time = (ed[0]-st[0])*60 + (ed[1]-st[1])
        melody = parse(melody)
        oset = time//len(melody)
        mod = time%len(melody)
        melody = melody*oset + melody[:mod]
        ht[melody] = nm
        if m in melody:
            if catch[0] < time:
                catch = [time,ht[melody]]
    if catch[0]:
        return catch[1]
    else:
        return '(None)'