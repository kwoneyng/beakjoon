var map = (n,arr)=>{
    var board = []
    arr.forEach(item =>{
        var res = item.toString(2)
        var plus = ''
        if (res.length < n){
            for (var i=0;i<n-res.length;i++){
                plus+='0'
            }
            res = plus + res
        }
        board.push(res)
    })
    return board
}
function solution(n, arr1, arr2) {
    var map1 = map(n,arr1)
    var map2 = map(n,arr2)
    var answer = []
    for (var i=0; i<n; i++){
        var row = ''
        for (var j=0; j<n; j++){
            if (map1[i][j] === '0' & map2[i][j] === '0'){
                row += ' '
            } else{
                row += '#'
            }
        }
        answer.push(row)
    }
    
    return answer;
}