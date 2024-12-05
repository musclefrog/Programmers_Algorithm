function solution(citations) {
    let hIndex = 0;
    citations.sort((a, b) => b - a); // 내림차순 정렬

    for (let i = 0; i < citations.length; i++) {
        if (i + 1 <= citations[i]) { // i + 1편이 citations[i]번 이상 인용되었는지 확인
            hIndex = i + 1;
        } else {
            break;
        }
    }

    return hIndex;
}