function LCM(n1, n2) {
    let lcm = 1;
    while(true) {
        if((lcm % n1 === 0) && (lcm % n2 === 0)) {
            break;
        }
        lcm++;
    }
    return lcm;
}

function solution(arr) {
    let stack = [];
    if(arr.length === 1) {
        stack.push(arr[0]);
    } else {
        let tmp = LCM(arr[0], arr[1]);
        let i = 1;
        stack.push(tmp);
        while(i < arr.length) {
            tmp = LCM(stack.pop(), arr[i]);
            stack.push(tmp);
            i++;
        }
    }
    return stack[0];
}