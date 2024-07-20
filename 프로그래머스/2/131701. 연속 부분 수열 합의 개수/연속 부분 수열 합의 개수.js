function solution(elements) {
    let arr = [];
    let elements2 = elements.concat(elements);
    
    for(let i=1; i<=elements.length; i++) {
        for(let j=0; j<elements.length; j++) {
            let sum = 0;
            sum = elements2.slice(j, (j+i)).reduce((a,b) => a+b, 0);
            arr.push(sum);
        }
    }
    const answer = new Set(arr);
    return answer.size;
}