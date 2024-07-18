function solution(k, tangerine) {
    let map = new Map();
    for (let t of tangerine) {
        if (map.has(t)) {
            map.set(t, map.get(t) + 1);
        } else {
            map.set(t, 1);
        }
    }
    let frequencies = [...map.values()].sort((a, b) => b - a);
    
    let add = 0;
    let cnt = 0;
    while(add < k) {
        add += frequencies[cnt];
        cnt++;
    }
    return cnt;
}