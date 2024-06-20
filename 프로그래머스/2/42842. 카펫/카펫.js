function solution(brown, yellow) {
    let w = (brown + 4 + Math.sqrt(Math.pow((-brown-4), 2) - 16*(brown + yellow)))/4;
    let h = (brown + 4 - Math.sqrt(Math.pow((-brown-4), 2) - 16*(brown + yellow)))/4;
    
    return [w, h];
}