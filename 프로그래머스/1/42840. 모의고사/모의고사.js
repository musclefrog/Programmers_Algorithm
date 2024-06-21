function solution(answers) {
    let result = [];
    let answer = [];
    const students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];
    for(let i=0; i<3; i++) {
        let cnt = 0;
        for(let j=0; j<answers.length; j++) {
            if(students[i][j % students[i].length] === answers[j]) {
                cnt++;
            }
        }
        result.push(cnt);
    }
    
    for(let k=0; k<3; k++) {
        if(result[k] === Math.max(...result)) {
        answer.push(k + 1);
        }
    }
    
    return answer.sort((a, b) => a - b);
}