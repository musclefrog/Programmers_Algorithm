function solution(s) {
    let answer = [];
    while(s !== '1') {
        let cntZero = s.split('').filter((el) => el === '0').length;
        let cntOne = s.length - cntZero;
        s = cntOne.toString(2);
        answer.push(cntZero);
    }
    return [answer.length, answer.reduce((a,b) => a+b, 0)];
}