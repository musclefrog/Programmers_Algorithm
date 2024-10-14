function solution(k, score) {
    let result = [];
    let best = [];
    
    for(let i = 0; i < score.length; i++) {
        if(i < k) {
            best.push(score[i]);
        }
        else {
            if(score[i] > Math.min(...best)) {
                best[best.indexOf(Math.min(...best))] = score[i];
            }
        }
        result.push(Math.min(...best));
    }
    return result;
}