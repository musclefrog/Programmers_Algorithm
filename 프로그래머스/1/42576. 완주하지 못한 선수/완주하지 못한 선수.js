function solution(participant, completion) {
    const hashMap = new Map();

    for(let i = 0; i < participant.length; i++) {
        let part = participant[i], 
            comp = completion[i];

        hashMap.set(part, (hashMap.get(part) || 0) + 1);
        hashMap.set(comp, (hashMap.get(comp) || 0) - 1);
    }
    for(let [key, value] of hashMap) {
        if(value > 0) return key;
    }
    return 'nothing';
}