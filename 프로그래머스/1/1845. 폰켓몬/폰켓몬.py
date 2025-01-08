def solution(nums):
    n_dict = dict() #hash
    for n in nums:
        n_dict[n] = 1 # 같은 종류의 폰켓몬의 중복이 제거
    if len(nums) // 2 <= len(n_dict):
        return len(nums) // 2
    return len(n_dict)