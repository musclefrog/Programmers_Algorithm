function solution(name, yearning, photo) {
    let answer = [];
    let dict = {};
    for(let i=0; i<name.length; i++) {
        dict[name[i]] = yearning[i];
    }
    for(let arr of photo) {
        let sum = 0;
        for(let man of arr) {
            if(name.includes(man)) {
                sum += dict[man];    
            }
        }
        answer.push(sum);
    }
    return answer;
}