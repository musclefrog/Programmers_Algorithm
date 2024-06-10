function solution(num_str) {
    return num_str.split('').map(el => parseInt(el)).reduce((a,b) => a+b, 0);
}