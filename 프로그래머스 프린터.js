function solution(priorities, location) {
    var answer = 0;
    priorities = priorities.map((item,index)=>{
        return [item, index]
    })
    while (priorities){
        var cur = priorities.shift()
        var max_p = 0
        priorities.forEach(item=>{
            if (max_p < item[0]) max_p = item[0]
        })
        if (cur[0] < max_p){
            priorities.push(cur)
        } else if(cur[1] === location){
            return answer+1
        } else {
            answer += 1
        }
    }
}