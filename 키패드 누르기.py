def wh(n,ht,lh,rh,lkey,rkey, hand):
    if n in lkey:
        lh = ht[n]
        return ht[n],'L'
    elif n in rkey:
        rh = ht[n]
        return ht[n],'R'
    else:
        target = ht[n]
        dl = abs(lh[0]-target[0]) + abs(lh[1]-target[1])
        dr = abs(rh[0]-target[0]) + abs(rh[1]-target[1])
        if dl > dr:
            rh = target
            return ht[n],'R'
        elif dr > dl:
            lh = target
            return ht[n],'L'
        else:
            if hand == 'right':
                rh = target
                return ht[n],'R'
            else:
                lh = target
                return ht[n],'L'
    

def solution(numbers, hand):
    answer = ''
    lh = [3,0]
    rh = [3,2]
    lkey = [1,4,7]
    rkey = [3,6,9]
    ht = {}
    for i in range(3):
        for j in range(1,4):
            ht[3*i+j] = [i,j-1]
    ht[0] = [3,1]    
    for n in numbers:
        key,result = wh(n,ht,lh,rh,lkey,rkey,hand)
        if result == 'L':
            lh = key
        else:
            rh =key
        answer += result
    
    return answer

n,h =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
print(solution(n,h))