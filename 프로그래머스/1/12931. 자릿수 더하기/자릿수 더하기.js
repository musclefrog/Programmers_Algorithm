function solution(n)
{
    const arr = String(n).split("")
    return arr.reduce((a,b) => Number(a) + Number(b), 0);
}