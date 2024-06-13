const solution = (G) => {
	let arr = [];
	let cnt = 0;
	let answer = '';
	while(G !== 0) {
		arr.push(G % 2);
		G = Math.floor(G / 2);
	}
	for(let i=0; i<arr.length; i++) {
		if(arr[i] === 1) {
			answer += i + ' ';
			cnt++;
		}
	}
	console.log(cnt);
	console.log(answer.slice(0, answer.length - 1));
};

const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let G = 0;
rl.on('line', (line) => {
	G = line;
	rl.close();
}).on('close', () => {
	solution(G);
	process.exit();
})