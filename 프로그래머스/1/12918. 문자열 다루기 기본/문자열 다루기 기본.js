function solution(s) {
    let answer = true;
    const arr = s.split('');
    
    if(arr.length === 4 || arr.length === 6){
        for(let i=0; i<arr.length; i++){
            if(isNaN(arr[i])){
                answer = false;
                break;
            }
        }
    } else {
        answer = false;
    }
    return answer;
}