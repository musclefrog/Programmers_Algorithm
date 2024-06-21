function binary(num) {
    let oneCnt = 0;
    while(num !== 0) {
        if(num % 2 === 1) {
            oneCnt++;
        }
        num = Math.floor(num / 2);
    }
    return oneCnt;
}

function solution(n) {
    const binN = binary(n);
    let i = n + 1;
    while(true) {
        if(binN === binary(i)) {
            break;
        }
        i++;
    }
    return i;
}