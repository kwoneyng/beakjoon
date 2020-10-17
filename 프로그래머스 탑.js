function solution(heights) {
    var answer = [];
    heights.forEach((height,idx) => {
        if (idx === 0){
            answer.push(0)
        } else{
            while(idx >= 0){
                idx -= 1
                if (idx < 0){
                    answer.push(0)
                    break
                } else if (heights[idx] > height){
                    answer.push(idx+1)
                    break
                }
            }
        }
    })
    return answer;
}
