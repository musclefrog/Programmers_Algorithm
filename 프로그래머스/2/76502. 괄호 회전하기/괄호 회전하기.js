function solution(s) {
    let answer = 0;
    const str = s.repeat(2);
    
    for(let i=0; i<s.length; i++) {
        let rotate = str.slice(i, i+s.length).split('');
        let stack = [];
        stack.push(rotate[0]);
        for(let j=1; j<rotate.length; j++) {
            switch (rotate[j]) {
                case ']':
                    if(stack[stack.length - 1] === '[') {
                        stack.pop();
                    }
                    break;
                case ')':
                    if(stack[stack.length - 1] === '(') {
                        stack.pop();
                    }
                    break;
                case '}':
                    if(stack[stack.length - 1] === '{') {
                        stack.pop();
                    }
                    break;
                default:
                    stack.push(rotate[j]);
            }
        }
        if(stack.length === 0) {
            answer++;
        }
    }
    return answer;
}