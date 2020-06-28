def perm(dist,pre,arr):
    if len(dist) == 0:
        arr.append(pre)
        return
    for i in range(len(dist)):
        perm(dist[:i]+dist[i+1:],pre + [dist[i]], arr)

def solution(n, weak, dist):
    dist.sort(reverse=True)
    for t in range(1,len(dist)+1):
        person = []
        perm(dist[:t],[],person)
        # print(person)
        for per in person:
            for i in range(len(weak)):
                people = per[:]
                temp = weak[i:] + [n+weak[i] for i in range(0,i)]
                while temp and people:
                    d = people.pop(0) + temp[0]
                    while temp and temp[0] <= d:
                        temp.pop(0)
                if not temp:
                    return t
    return -1