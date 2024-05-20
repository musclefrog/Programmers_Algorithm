function solution(arr, divisor) {
    return arr.filter(x => x % divisor === 0).length ? arr.filter(x => x % divisor === 0).sort((a,b) => a-b) : [-1];
}