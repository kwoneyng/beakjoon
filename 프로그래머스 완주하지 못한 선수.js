function solution(participant, completion) {
    var answer = '';
    var total = {}
    var minus = {}
    for (var p of participant){
        if (total[p] === undefined){
            total[p] = 1
        } else{
            total[p] += 1
        }
    }
    for (var c of completion){
        if(minus[c] === undefined){
            minus[c] = 1
        } else{
            minus[c] +=1
        }
    }
    for (var p of participant){
        if (total[p] !== minus[p]){
            return p
        }
    }
}