function cal(n, m) {
    let gcd = 0;
    let i = 1;
    while(i <= Math.min(n, m)) {
        if(n % i === 0 && m % i === 0) {
            gcd = i;
        }
        i++;
    }
    let lcm = gcd * (n / gcd) * (m / gcd);
    return [gcd, lcm];
}

function solution(n, m) {
    return cal(n, m);
}