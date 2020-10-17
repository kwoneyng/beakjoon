function make_answer(time){
    var hour = parseInt(time/60)+''
    var min = time%60+''
    if(hour.length === 1){
        hour = '0'+hour
    }
    if(min.length === 1){
        min = '0'+min
    }
    return hour+':'+min
}

function solution(n, t, m, timetable) {
    var answer = '';
    timetable = timetable.map((time)=>{
        var t = time.split(":")
        return t[0]*60 + t[1]*1
    })
    timetable.sort((a,b)=>{
        return a-b
    })
    var cur_time = 9*60
    for (var i=0; i<n; i++){
        var on_bus = []
        for (var j=0; j<m; j++){
            if (timetable[0] <= cur_time){
                on_bus.push(timetable.shift())
            } else break
        }
        cur_time += t
        if (on_bus.length === 0 & timetable.length === 0){
            return make_answer(9*60 + ((n-1)*t))
        }
    }
    var len = on_bus.length
    if (len === m){
        var time = on_bus[len-1]-1
        return make_answer(time)
    } else {
        return make_answer(9*60 + ((n-1)*t)) 
    }
}