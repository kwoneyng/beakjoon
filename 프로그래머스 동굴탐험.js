function solution(n, path, order) {
    var nxt_arr = []
    var ord_arr = []
    var unord_arr = []
    for (var i=0;i<n; i++){
        nxt_arr.push([])
        ord_arr.push([])
        unord_arr.push([])
    }
    path.forEach(item=>{
        nxt_arr[item[0]].push(item[1])
        nxt_arr[item[1]].push(item[0])
    })
    order.forEach(item=>{
        ord_arr[item[1]].push(item[0])
        unord_arr[item[0]].push(item[1])
    })
    var q = [0]
    var vis = []
    for (var i=0; i<n; i++){
        vis.push(0)
    }
    vis[0] = 1
    while (q.length > 0){
        var node = q.shift()
        for (var i=0; i<nxt_arr[node].length; i++){
            var nxt = nxt_arr[node][i]
            if (ord_arr[nxt].length > 0){
                for (var j=0; j<ord_arr[nxt];j++){
                    var ord = ord_arr[nxt][j]
                    if (vis[ord] === 1){
                        if (vis[nxt] === 0){
                            q.push(nxt)
                            vis[nxt] = 1
                        }
                    } else {
                        vis[nxt] = -1
                    }
                }
            } else {
                if (vis[nxt] === 0 || nxt === 0){
                    q.push(nxt)
                    vis[nxt] = 1
                    for (var k=0; k < unord_arr[nxt].length; k++){
                        var unord = unord_arr[nxt][k]
                        if (vis[unord] === -1){
                            q.push(unord)
                            vis[unord] = 1
                        }
                    }
                }
            }
        }
    }
    var rs = 0
    vis.forEach(item=>{
        if (item === 0){
            rs += 1
        }
    })   
    if (rs>0){
        return false
    } else{
        return true
    }
}

var n = 9
var path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	
var order = [[8,5],[6,7],[4,1]]
console.log(solution(n,path,order))