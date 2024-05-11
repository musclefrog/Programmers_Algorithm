function solution(s, n) {
    var answer = '';
    const upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const loAlpha = "abcdefghijklmnopqrstuvwxyz";
    const arr = s.split("");
    
    for(str of arr){
        if(upAlpha.includes(str)) {
            answer += upAlpha[(upAlpha.indexOf(str) + n) % 26];
        } else if(loAlpha.includes(str)) {
            answer += loAlpha[(loAlpha.indexOf(str) + n) % 26];
        } else {
            answer += ' ';
        }
    }
    
    return answer;
}