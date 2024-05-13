let result = [];

function hanoi(N, start, to, via) {
    if(N === 1) {
        result.push([start, to]);
    } else {
        hanoi(N-1, start, via, to);
        hanoi(1, start, to);
        hanoi(N-1, via, to, start);
    }
}
function solution(n) {
    hanoi(n, 1, 3, 2);
    return result;
}