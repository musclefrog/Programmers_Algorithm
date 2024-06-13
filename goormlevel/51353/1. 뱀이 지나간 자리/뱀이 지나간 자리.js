const solution = (data) => {
	const [N, M] = data;
	const A = '#'.repeat(M);
	const B = '.'.repeat(M-1) + '#';
	const C = '#' + '.'.repeat(M-1);
	
	for(let i=0; i<N; i++) {
		if(i % 2 === 0) {
			console.log(A);
		} else {
			if (i % 4 === 1) {
				console.log(B);
			} else {
				console.log(C);
			}
		}
	}
};

const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let data = [];
rl.on('line', (line) => {
	data = line.split(" ").map((el) => parseInt(el));
	rl.close();
}).on('close', () => {
	solution(data);
	process.exit();
});