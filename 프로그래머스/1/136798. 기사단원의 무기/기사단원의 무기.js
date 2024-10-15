function solution(number, limit, power) {
    let divCnt = [];
    
    // 약수 배열 생성
    for(let num=1; num<=number; num++) {
        let i = 1;
        let divArr = [];
        while(i <= Math.sqrt(num)) {
            if(num % i === 0) {
                divArr.push(i);
                if(num / i !== i) {
                    divArr.push(num / i);
                }
            }
            i++;
        }
        divCnt.push(divArr.length);
    }
    
    // limit을 초과하는 기사는 power로 바꾸어서 더하기
    let arr = divCnt.map((x) => x > limit ? power : x);
    return arr.reduce((a,b) => a+b, 0);
}