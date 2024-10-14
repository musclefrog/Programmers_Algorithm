function solution(s) {
    let answer = [];
    for(let i = 0; i < s.length; i++) {
        answer.push(s.slice(0, i).includes(s[i]) ? i - s.slice(0, i).lastIndexOf(s[i]) : -1);
    }
    return answer;
}