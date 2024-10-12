function solution(num) {
    let cnt = 0;
    while(num !== 1) {
        num = num % 2 === 0 ? num / 2 : num * 3 + 1;
        cnt ++;
        if (cnt === 500) break;
    }
    return cnt >= 500 ? -1 : cnt;
}