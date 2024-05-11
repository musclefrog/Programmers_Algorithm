function solution(s) {
    let answer = s;
    const num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    for(let i = 0; i < num.length; i++) {
        let arr = answer.split(num[i]);
        answer = arr.join(i);
    }
    return Number(answer);
}