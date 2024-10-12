function solution(a, b) {
    return [...Array(Math.abs(a - b) + 1).keys()].map(key => key + Math.min(a, b)).reduce((x,y) => x+y, 0);
}