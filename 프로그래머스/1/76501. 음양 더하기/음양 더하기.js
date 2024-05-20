function solution(absolutes, signs) {
    let result = 0;
    absolutes.forEach((v,i) => {
        if(signs[i]) { result += v; }
        else { result -= v; }
    })
    return result;
}