function solution(s) {
    let answer = true;
    const arr = s.split('');
    if (s.length === 4 || s.length === 6) {
        for (let i=0; i<arr.length; i++) {
            if(isNaN(arr[i])) {
                answer = false;
                break;
            }
        }
    } else { answer = false; }
    return answer;
}