function solution(numbers) {
    const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    return arr.filter(x => !numbers.includes(x)).reduce((a,b) => a + b, 0);
}