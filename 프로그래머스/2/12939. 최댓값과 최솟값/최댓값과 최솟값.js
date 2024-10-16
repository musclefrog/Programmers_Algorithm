function solution(s) {
    let num = s.split(' ').map(x => parseInt(x));
    return `${Math.min(...num)} ${Math.max(...num)}`;
}