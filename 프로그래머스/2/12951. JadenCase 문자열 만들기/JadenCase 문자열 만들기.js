function solution(s) {
    let answer = [];
    s = s.split(" ");
    for(let str of s) {
        if(str !== '') {
            str = str[0].toUpperCase() + str.slice(1).toLowerCase();
        }
        answer.push(str);
    }
    return answer.join(" ");
}