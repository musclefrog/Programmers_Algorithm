function solution(numbers, hand) {
    let answer = '';
    const leftNum = [1, 4, 7, '*'];
    const midNum = [2, 5, 8, 0];
    const rightNum = [3, 6, 9, '#'];
    
    let leftNow = '*';
    let rightNow = '#';
    let leftDistance = 0;
    let rightDistance = 0;
    
    for(num of numbers) {
        if(leftNum.includes(num)) {
            answer += 'L';
            leftNow = num;
        } else if(rightNum.includes(num)) {
            answer += 'R';
            rightNow = num;
        } else if(midNum.includes(num)) {
            if(leftNum.includes(leftNow)) {
                leftDistance = Math.abs(midNum.indexOf(num) - leftNum.indexOf(leftNow)) + 1;
            } else if(midNum.includes(leftNow)) {
                leftDistance = Math.abs(midNum.indexOf(num) - midNum.indexOf(leftNow));
            }
            if(rightNum.includes(rightNow)) {
                rightDistance = Math.abs(midNum.indexOf(num) - rightNum.indexOf(rightNow)) + 1;
            } else if(midNum.includes(rightNow)) {
                rightDistance = Math.abs(midNum.indexOf(num) - midNum.indexOf(rightNow));
            }
            if(leftDistance === rightDistance) {
                if(hand === "right") {
                    answer += 'R';
                    rightNow = num;
                } else if(hand === "left") {
                    answer += 'L';
                    leftNow = num;
                }
            } else if(leftDistance > rightDistance) {
                answer += 'R';
                rightNow = num;
            } else if(rightDistance > leftDistance) {
                answer += 'L';
                leftNow = num;
            }
        }
    }
    return answer;
}