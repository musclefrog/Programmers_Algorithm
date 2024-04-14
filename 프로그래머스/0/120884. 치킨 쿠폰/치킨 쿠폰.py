def solution(chicken):
    answer = 0
    newCoupon = chicken
    remainCoupon = 0
    while newCoupon + remainCoupon >= 10:
        tmp1 = (newCoupon + remainCoupon) // 10
        tmp2 = (newCoupon + remainCoupon) % 10
        newCoupon = tmp1
        remainCoupon = tmp2
        answer += newCoupon
    return answer