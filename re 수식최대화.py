def calc(nbs,oprd,i,j,k):
    for key in [i,j,k]:
        nnbs = [nbs.pop(0)]
        noprd = []
        for _ in range(len(nbs)):
            nxop = oprd.pop(0)
            nxn = nbs.pop(0)
            if nxop == key:
                if key == '-':
                    nnbs.append(nnbs.pop()-nxn)
                elif key == '+':
                    nnbs.append(nnbs.pop()+nxn)
                else:
                    nnbs.append(nnbs.pop()*nxn)
            else:
                noprd.append(nxop)
                nnbs.append(nxn)
        nbs = nnbs
        oprd = noprd
    return nbs[0]    
    
def solution(expression):
    nbs = []
    oprd = []
    su = ''
    for i in expression:
        if i.isdigit():
            su += i
        else:
            oprd.append(i)
            nbs.append(int(su))
            su = ''
    nbs.append(int(su))
    keys = ['-','*','+']
    awards = 0
    for i in keys:
        for j in keys:
            for k in keys:
                if i != j and j != k and i != k:
                    tnbs = nbs[:]
                    toprd = oprd[:]
                    awards = max(awards,abs(calc(tnbs,toprd,i,j,k)))
    
    return awards

ep = "100-200*300-500+20"
print(solution(ep))