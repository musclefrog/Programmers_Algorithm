function solution(n) {
    let x = 1;
    while(n % x != 1) {
        x += 1;
    }
    return x;
}