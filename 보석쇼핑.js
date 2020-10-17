function solution(gems) {
    var answer = [0,100000];
    var total = new Set(gems).size
    var ht = {}
    var start = 0
    gems.forEach((item,i)=>{
        if(!ht[item]){
            ht[item] = 1
        } else {
            ht[item] += 1
        }
        if (Object.keys(ht).length === total){
            while (start <= i){
                if(ht[gems[start]]-1>0){
                    ht[gems[start]] -= 1
                    start += 1
                } else if(answer[1]-answer[0] > i-start){
                    answer = [start+1,i+1]
                    break
                } else break
            }
        }
        
    })
    return answer;
}

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
console.log(solution(gems))