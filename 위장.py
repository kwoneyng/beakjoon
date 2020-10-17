from itertools import combinations

def solution(clothes):
    answer = 0
    ht = {}
    arr = []
    for c in clothes:
        if ht.get(c[1]):
            ht[c[1]].append(c[0])
        else:
            ht[c[1]] = [c[0]]
    for key in ht.keys():
        arr.append(len(ht[key]))
    answer += sum(arr)
    rs = []
    for i in range(1,len(arr)+1):
        rs.append(combinations(arr,i))
    return answer