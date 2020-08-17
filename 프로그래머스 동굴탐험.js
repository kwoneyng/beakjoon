function solution(n, path, order) {
    let nxtArr = Array.from({length:n}, ()=>[])
    let ordArr = Array.from({length:n}, ()=>0)
    let relArr = Array.from({length:n}, ()=>0)
    let vis = Array.from({length:n}, ()=>0)
    vis[0] = 1
    path.forEach(([a,b])=>{
        nxtArr[a].push(b)
        nxtArr[b].push(a)
    })
    order.forEach(([a,b])=>{
        ordArr[b] = a
        relArr[a] = b        
    })
    let q = [0]
    while (q.length !== 0){
        let node = q.shift()
        if (vis[ordArr[node]]){
            vis[node] = 1
            if (nxtArr[node].length > 1 || node === 0){
                for (const nxt of nxtArr[node]){
                    if (vis[nxt] === 0){
                        q.push(nxt)
                    }
                }
            }
            if (relArr[node] !== 0 && vis[relArr[node]] === -1){
                q.push(relArr[node])
            }
        } else {
            vis[node] = -1
        }
    }
    for (const i of vis){
        if(i <= 0){
            return false
        }
    }
    return true;
}

var n = 9
var path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	
var order = [[8,5],[6,7],[4,1]]
console.log(solution(n,path,order))