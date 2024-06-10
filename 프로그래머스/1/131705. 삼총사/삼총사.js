function solution(number) {
    let answer = 0;
    for(let idx=0; idx<number.length - 2; idx++) {
        for(let x=idx+1; x<number.length - 1; x++) {
            for(let y=x+1; y<number.length; y++) {
                if(number[idx] + number[x] + number[y] === 0) {
                    answer++;
                }
            }
        }
    }
    return answer;
}