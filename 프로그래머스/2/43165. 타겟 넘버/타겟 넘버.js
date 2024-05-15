function solution(numbers, target) {
    let cnt = 0;
    function dfs(numbers, target, idx, values) {
        if(idx === numbers.length && values === target) {
            cnt += 1;
            return;
        } else if(idx === numbers.length) {
            return;
        }
        dfs(numbers, target, idx + 1, values + numbers[idx]);
        dfs(numbers, target, idx + 1, values - numbers[idx]);
    }
    dfs(numbers, target, 0, 0);
    return cnt;
}