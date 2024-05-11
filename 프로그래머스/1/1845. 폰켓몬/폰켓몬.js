function solution(nums) {
    const numsSet = new Set(nums);
    const n = nums.length / 2;
    return numsSet.size >= n ? n : numsSet.size;
}