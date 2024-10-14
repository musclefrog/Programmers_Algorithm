function solution(s) {
    const words = s.split(" ");
    let answer = '';
    for(let word of words) {
        for(let i = 0; i < word.length; i++) {
            answer += i % 2 === 0 ? word[i].toUpperCase() : word[i].toLowerCase();
        }
        answer += ' ';
    }
    return answer.slice(0, answer.length - 1);
}