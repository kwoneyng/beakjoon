function solution(N, stages) {
    var deck = []
    for (var i=0; i <N+1; i++){
        deck.push(0)
    }
    stages.forEach(i=>{
        deck[i-1] += 1    
    })
    // return deck
    var answer = [];
    var P = stages.length
    for (var i=0; i< N+2; i++){
        if (deck[i]){
            var temp = deck[i]
            deck[i] = temp/P
            P -= temp
        }
    }
    deck[N] = -1
    for (var i=0;i < N; i++){
        var target = Math.max.apply(this,deck)
        answer.push(deck.indexOf(target)+1)
        deck[deck.indexOf(target)] = -1
    }
    
    // return deck
    return answer;
}