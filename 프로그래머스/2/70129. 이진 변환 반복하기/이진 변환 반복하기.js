function binary(num) {
    let arr = [];
    while(num !== 0) {
        arr.push(num % 2);
        num = Math.floor(num / 2);
    }
    return arr.reverse().join('');
}

function solution(s) {
    let answer = [];
    while(s !== '1') {
        let cntZero = s.split('').filter((el) => el === '0').length;
        let cntOne = s.length - cntZero;
        s = binary(cntOne);
        answer.push(cntZero);
    }
    return [answer.length, answer.reduce((a,b) => a+b, 0)];
}