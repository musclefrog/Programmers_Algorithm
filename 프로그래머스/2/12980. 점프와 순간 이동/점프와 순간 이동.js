function solution(n) {
    let jump = 0;
    while(n !== 0) {
        if(n % 2 === 1) {
            n = (n - 1) / 2;
            jump++;
        } else {
            n /= 2;
        }
    }
    return jump;
}