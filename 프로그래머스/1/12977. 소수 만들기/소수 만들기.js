function isPrimeNumber(num) {
    let cnt = 0;
    let result = false;
    for(let x=1; x<=num; x++) {
        if(num % x === 0) {
            cnt++;
        }
    }
    if(cnt === 2) {
        result = true;
    }
    return result;
}
function solution(nums) {
    let answer = 0;
    for(let i=0; i<nums.length-2; i++) {
        for(let j=i+1; j<nums.length-1; j++) {
            for(let k=j+1; k<nums.length; k++) {
                if(isPrimeNumber(nums[i] + nums[j] + nums[k])) {
                    answer++;
                }
            }
        }
    }
    return answer;
}