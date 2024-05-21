function solution(begin, target, words) {
    const visited = {[begin] : 0};
    const queue = [begin];
    
    while(queue.length) {
        const cur = queue.shift();
        if(cur === target) break;
        for(const word of words) {
            if(isConnected(cur, word) && !visited[word]) {
                visited[word] = visited[cur] + 1;
                queue.push(word);
            }
        }
    }
    return visited[target] ? visited[target] : 0;
}

function isConnected(str1, str2) {
    let cnt = 0;
    for(let i=0; i<str1.length; i++) {
        if(str1[i] !== str2[i]) cnt++;
    }
    return cnt === 1 ? true : false;
}