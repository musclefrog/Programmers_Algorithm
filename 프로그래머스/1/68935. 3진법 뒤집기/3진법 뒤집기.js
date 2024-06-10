function solution(n) {
    let answer = 0;
    let arr =[];
    
    while(n !== 0){
        arr.push(n % 3);
        n = Math.floor(n / 3);
    }
    for(let i=0; i<arr.length; i++) {
        answer += arr[i] * Math.pow(3, arr.length - i - 1);
    }
    return answer;
}