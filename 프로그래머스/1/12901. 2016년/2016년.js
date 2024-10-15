function solution(a, b) {
    const months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
    let arr = months.slice(0, a);
    let day = (arr.reduce((x,y) => x+y, 0) + b) % 7;
    return days[day];
}