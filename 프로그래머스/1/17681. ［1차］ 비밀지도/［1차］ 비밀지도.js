function solution(n, arr1, arr2) {
    let answer = [];
    // '#'로 채워진 2차원 배열 생성. 지도 1과 지도 2를 합친 결과를 표현.
    const newArr = Array.from(Array(n), () => Array(n).fill('#'));
    
    // 지도를 2진수로 변환하는 함수.
    function binary(arr) {
        let binArr = [];
        for(let i = 0; i < n; i++) {
            let binNum = arr[i].toString(2);
            binArr.push(binNum.split(""));
            for(let j = 0; j < n - binNum.length; j++) {
                binArr[i].unshift('0');
            }
        }
        return binArr;
    }
    
    // 지도 1과 지도 2 생성.
    binArr1 = binary(arr1);
    binArr2 = binary(arr2);
    
    // 지도 1과 지도 2를 합친 지도 생성.
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(binArr1[i][j] === '0' && binArr2[i][j] === '0') {
                newArr[i][j] = ' ';
            }
        }
    }
    
    // 새로운 지도의 2차원 배열을 1차원 문자열 배열로 만들어줌.
    for(let s of newArr) {
        let k = s.join('');
        answer.push(k);
    }
    return answer;
}

