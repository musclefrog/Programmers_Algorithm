function solution(t, p) {
    let cnt = 0;
    for(let i=0; i<t.length-p.length+1; i++){
        cnt += +t.slice(i, i + p.length) <= p ? 1 : 0;
    }
    return cnt;
}