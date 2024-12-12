function solution(clothes) {
    let map = new Map();
    for(let i=0; i<clothes.length; i++) {
        if(!map.get(clothes[i][1])) {
            map.set(clothes[i][1], 1);
        } else {
            map.set(clothes[i][1], map.get(clothes[i][1]) + 1);
        }
    }
    
    const arr = Array.from(map.values());
    let answer = 1;
    for(let j=0; j<arr.length; j++) {
        answer *= (arr[j] + 1);
    }
    return answer - 1;
}