function solution(want, number, discount) {
    let result = 0;
    
    for(let i = 0; i < discount.length - 9; i++) {
        let arr = Array(want.length).fill(0);
        let membership = discount.slice(i, i+10);
        
        for(let j = 0; j < want.length; j++) {
            arr[j] = membership.filter(el => el === want[j]).length;
        }
        
        if(arr.toString() === number.toString()) {
            result++;
        }
    }
    return result;
}