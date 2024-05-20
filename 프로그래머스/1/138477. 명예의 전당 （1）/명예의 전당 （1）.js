function solution(k, score) {
    let result = [];
    let best = [];
    let i = 0;
    
    while(i < score.length) {
        if(i < k) {
            best.push(score[i]);
        }
        else {
            if(score[i] > Math.min(...best)) {
                best[best.indexOf(Math.min(...best))] = score[i];
            }
        }
        result.push(Math.min(...best));
        i++;
    }
    return result;
}