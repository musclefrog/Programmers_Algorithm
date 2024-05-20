function solution(a, b, n) {
    let newBottle = n;
    let remainBottle = 0;
    let coke = 0;
    let tmp1 = 0;
    let tmp2 = 0;
    
    while(newBottle + remainBottle >= a) {
        tmp1 = Math.floor((newBottle + remainBottle) / a) * b;
        tmp2 = (newBottle + remainBottle) % a;
        newBottle = tmp1;
        remainBottle = tmp2;
        coke += newBottle;
    }
    return coke;
}