function solution(array, commands) {
    let answer = [];
    for(command of commands) {
        let arr = array.slice(command[0]-1, command[1]);
        arr.sort((a,b) => a-b);
        answer.push(arr[command[2]-1]);
    }
    return answer;
}