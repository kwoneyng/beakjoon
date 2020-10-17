def solution(gems):
    answer = [0,100000]
    total = len(set(gems))
    ht = {}
    start = 0
    for i in range(len(gems)):
        gem = gems[i]
        if ht.get(gem):
            ht[gem]+=1
        else:
            ht[gem]=1
        if len(ht) == total:
            while start<=i:
                if ht[gems[start]]-1>0:
                    ht[gems[start]] -= 1
                    start += 1
                elif answer[1]-answer[0] > i-start:
                    answer = [start+1,i+1]
                    break
                else :
                    break
        
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)