function solution(s) {
    let words = s.split(" ");
    let answer = '';
    for(let word of words) {
        for(let i=0; i<word.length; i++) {
            if(i % 2 === 0) {
                answer += word[i].toUpperCase();
            } else {
                answer += word[i].toLowerCase();
            }
        }
        answer += ' ';
    }
    return answer.slice(0, answer.length - 1);
}