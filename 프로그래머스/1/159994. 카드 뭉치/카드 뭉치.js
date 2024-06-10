function solution(cards1, cards2, goal) {
    let answer = 'Yes';
    let usedCards1 = [];
    let usedCards2 = [];
    for(let word of goal) {
        if(cards1.includes(word)) {
            usedCards1.push(cards1.indexOf(word));
        } else if(cards2.includes(word)) {
            usedCards2.push(cards2.indexOf(word));
        }
    }
    const usedCards = [usedCards1, usedCards2];
    
    for(let usedCard of usedCards) {
        for(let i=0; i<usedCard.length-1; i++) {
            if(usedCard[i] > usedCard[i+1] || usedCard[i] === usedCard[i+1] || usedCard[i+1] - usedCard[i] > 1) {
                answer = 'No';
                break;
            }
        }
    }
    return answer;
}