function solution(chicken) {
    let newCoupon = chicken;
    let remainCoupon = 0;
    let service = 0;
    let tmp1 = 0;
    let tmp2 = 0; 
    
    while(newCoupon + remainCoupon >= 10){       
        tmp1 = Math.floor((newCoupon + remainCoupon) / 10);
        tmp2 = (newCoupon + remainCoupon) % 10;
        newCoupon = tmp1;
        remainCoupon = tmp2;
        service += newCoupon;
    }
    return service;
}