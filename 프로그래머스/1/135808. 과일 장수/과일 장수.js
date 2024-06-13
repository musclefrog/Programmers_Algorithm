function solution(k, m, score) {
    let answer = 0;
    const boxCnt = Math.floor(score.length / m);
    const box = score.sort((a,b) => b-a).slice(0, boxCnt * m);
    for(let i=m-1; i<boxCnt*m; i+=m) {
        answer += box[i] * m;
    }
    return answer;
}