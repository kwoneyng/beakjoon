def find(item, cht, pht):
    if pht.get(item):
        return
    else:
        pht[item] = 1
        if cht.get(item):
            for nxt in cht[item]:
                find(nxt,cht,pht)
            

def solution(n, results):
    answer = 0
    wht = {}
    lht = {}
    for w,l in results:
        if wht.get(w):
            wht[w].append(l)
        else:
            wht[w] = [l]
        if lht.get(l):
            lht[l].append(w)
        else:
            lht[l] = [w]
            
    for i in range(1,n+1):
        win = {}
        lose = {}
        if wht.get(i):
            for nxt in wht[i]:
                find(nxt,wht,win)
        if lht.get(i):
            for nxt in lht[i]:
                find(nxt,lht,lose)
        if len(win) + len(lose) == n-1:
            answer += 1
    return answer

n, results = 5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))