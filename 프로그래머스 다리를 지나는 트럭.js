function sum(array){
    var result = 0
    array.forEach(item =>{
        result+=item
    })
    return result
}

function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var q = []
    var timer = []
    while (truck_weights.length > 0 | timer.length > 0){
        answer += 1
        if(timer.length > 0 & timer[0] === bridge_length){
            timer.shift()
            q.shift()
        }
        if (truck_weights.length > 0 & sum(q) + truck_weights[0] <= weight){
            q.push(truck_weights.shift())
            timer.push(0)
        }
        for (var i=0; i<timer.length; i++){
            timer[i] += 1
        }
    }
    return answer;
}

var bridge_length, weight, truck_weights
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length,weight,truck_weights)