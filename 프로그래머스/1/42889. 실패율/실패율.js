function solution(N, stages) {
    var answer = [];
    
    // 실패율 딕셔너리 선언
    let failRate = {};
    
    // 각 스테이지의 실패율 딕셔너리에 저장
    for (let stage=1; stage<=N; stage++) {
        failRate[stage] = stages.filter(x => x === stage).length / stages.filter(x => x >= stage).length
    }
    
    // 실패율 딕셔너리를 배열 형태로 바꾸고 Value 값으로 내림차순 정렬
    let sorted = Object.entries(failRate).sort((a, b) => b[1] - a[1]);
    
    // 정렬된 배열의 key값(element[0])을 새로운 배열에 넣어줌
    for(let element of sorted) {
        answer.push(Number(element[0]))
    }
    
    return answer;
}