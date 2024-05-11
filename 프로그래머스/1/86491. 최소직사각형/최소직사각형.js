function solution(sizes) {
    let short = [];
    let long = [];
    for(size of sizes) {
        short.push(Math.min(...size));
        long.push(Math.max(...size));
    }
    return Math.max(...short) * Math.max(...long);
}