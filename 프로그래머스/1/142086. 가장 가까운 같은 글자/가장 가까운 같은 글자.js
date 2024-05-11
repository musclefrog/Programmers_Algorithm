function solution(s) {
    let answer = [];
    
    for(let i = 0; i < s.length; i++) {
        if(s.slice(0, i).includes(s[i])) {
            answer.push(i - s.slice(0, i).lastIndexOf(s[i]));
        } else {
            answer.push(-1);
        }
    }
    return answer;
}